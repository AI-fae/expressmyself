from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from db import models
from db.db_setup import get_db
from sqlalchemy.orm import Session
from schemas.article_schema import Articles, DisplayArticle
from dependencies.oauth2 import get_current_user

router = APIRouter()


@router.post("/{creator_id}/article", 
            status_code=status.HTTP_201_CREATED,
            response_model=DisplayArticle)
def create_blog(creator_id:int, request:Articles, 
                db: Session = Depends(get_db), 
                current_user: Articles = Depends(get_current_user)):

    """Creates a new article and returns details of that article.
    Args:
        creator_id (str): A unique identifier of an of the creator's object in the database
        db (Session): The sqlite database for storing the article object
        current_user: An authenticator that validates the article creator
    Returns:
        HTTP_201_CREATED (new_blog): {key value pair of new article info}
    Raises
       HTTP_404_NOT_FOUND: creator_id not found in the User table
    """
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

@router.get("/all_articles", responses={200:{"model":Articles}})
def get_all_articles(db: Session = Depends(get_db),
                     current_user: Articles = Depends(get_current_user)):
    """fetches all articles stored in the database.
    Args:
        db (Session): The sqlite database for storing the article object
        current_user: An authenticator that validates the article creator
    Returns:
        HTTP_201_CREATED (new_blog): {key value pair of new article info}
    """
    blogs = (db.query(models.Articles).all())
    return blogs

@router.delete("/{id}/article", status_code=status.HTTP_200_OK)
def delete_article(id: int, db: Session= Depends(get_db), 
                current_user: Articles = Depends(get_current_user)):
    """deletes an article with id {id}.
    Args:
        id (str): A unique identifier of an of the article object 
            in the database to be deleted
        db (Session): The sqlite database for storing the article object
        current_user: An authenticator that validates the article creator
    Returns:
        HTTP_201_CREATED (new_blog): {key value pair of new article info}.
    Raises
       HTTP_404_NOT_FOUND: article does not exist
    """
    blog= db.query(models.Articles).filter(models.Articles.id ==id)
    if not blog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"article with id {id} doesn't exist")

    blog.delete(synchronize_session=False)
    db.commit()
    return JSONResponse({"detail": f"blog with id {id} successfully deleted"},
                 status_code=status.HTTP_200_OK)


@router.put("/{id}/article", status_code=status.HTTP_202_ACCEPTED)
def update_article(id:int, request:Articles, db: Session= Depends(get_db),
                 current_user: Articles = Depends(get_current_user)):
    """enables editing of and article with id {id}.
    Args:
        id (str): A unique identifier of an of the article object 
            in the database to be deleted
        db (Session): The sqlite database for storing the article object
        current_user: An authenticator that validates the article creator
    Returns:
        HTTP_202_ACCEPTED: update successful
    Raises
       HTTP_404_NOT_FOUND: article does not exist
    """
    blog= db.query(models.Articles).filter(models.Articles.id == id)
    if not blog.first(): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"blog with id {id} doesn't exist")

    blog.update({"title":request.title, "body":request.body}, 
                synchronize_session=False)
    db.commit()
    return JSONResponse({"detail": "blog successfully updated"},
                            status_code=status.HTTP_202_ACCEPTED)


@router.get("/{id}/article", responses={200:{"model":DisplayArticle}}, 
                response_model=DisplayArticle)
def single_article(id:int, db: Session= Depends(get_db), 
                current_user: Articles = Depends(get_current_user)):
    """fetches a single article with id {id}.
    Args:
        id (str): A unique identifier of an of the article object 
            in the database to be deleted
        db (Session): The sqlite database for storing the article object
        current_user: An authenticator that validates the article creator
    Returns:
        HTTP_200_OK: successful
    Raises
       HTTP_404_NOT_FOUND: article does not exist
    """
    blog = db.query(models.Articles).filter(
        models.Articles.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail= f"blog with id {id} not found")

    return blog