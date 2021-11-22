from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from db import models
from db.db_setup import get_db
from sqlalchemy.orm import Session
from schemas.article_schema import Blog, DisplayBlog
from dependencies.oauth2 import get_current_user

router = APIRouter()


@router.post("/{creator_id}/blog", status_code=status.HTTP_201_CREATED,
            response_model=DisplayBlog)
def create_blog(creator_id:int, request:Blog, db: Session = Depends(get_db), current_user: Blog = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.id == creator_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    detail=f"user with id {creator_id} doesn't exist")
    new_blog = models.Articles(
        title=request.title,
        body=request.body,
        creator_id= creator_id
    )
    db.add(new_blog)
    db.commit() 
    db.refresh(new_blog)
    return new_blog


@router.get("/all_blogs", responses={200:{"model":Blog}})
def get_all_articles(db: Session = Depends(get_db), current_user: Blog = Depends(get_current_user)):
    blogs = (db.query(models.Articles).all())
    return blogs

@router.delete("/{id}/blog", status_code=status.HTTP_200_OK)
def delete_blog(id: int, db: Session= Depends(get_db), current_user: Blog = Depends(get_current_user)):
    blog= db.query(models.Articles).filter(models.Articles.id ==id)
    if not blog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"blog with id {id} doesn't exist")

    blog.delete(synchronize_session=False)
    db.commit()
    return JSONResponse({"detail": f"blog with id {id} successfully deleted"},
                 status_code=status.HTTP_200_OK)


@router.put("/{id}/blog", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int, request:Blog, db: Session= Depends(get_db), current_user: Blog = Depends(get_current_user)):
    blog= db.query(models.Articles).filter(models.Articles.id == id)
    if not blog.first(): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"blog with id {id} doesn't exist")

    blog.update({"title":request.title, "body":request.body}, 
                synchronize_session=False)
    db.commit()
    return JSONResponse({"detail": "blog successfully updated"},
                            status_code=status.HTTP_202_ACCEPTED)


@router.get("/{id}/blog", responses={200:{"model":DisplayBlog}}, response_model=DisplayBlog)
def single_blog(id:int, db: Session= Depends(get_db), current_user: Blog = Depends(get_current_user)):
    blog = db.query(models.Articles).filter(
        models.Articles.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail= f"blog with id {id} not found")

    return blog