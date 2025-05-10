from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.deps import get_db
from database.models import AdCompaign
from database.schemas import AdCompaignCreate, AdCompaignOut, AdCompaignUpdate, AdCompaignPartialUpdate
from auth.auth import get_current_user

router = APIRouter(prefix="/adcompaigns", tags=["AdCompaigns"])

@router.post("/", response_model=AdCompaignOut)
def create_adcompaign(
    compaign: AdCompaignCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    db_compaign = AdCompaign(**compaign.dict())
    db.add(db_compaign)
    db.commit()
    db.refresh(db_compaign)
    return db_compaign

@router.get("/", response_model=list[AdCompaignOut])
def list_adcompaigns(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return db.query(AdCompaign).all()

@router.get("/{compaign_id}", response_model=AdCompaignOut)
def get_adcompaign(
    compaign_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    compaign = db.query(AdCompaign).filter(AdCompaign.id == compaign_id).first()
    if not compaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return compaign

@router.patch("/{compaign_id}", response_model=AdCompaignOut)
def patch_adcompaign(
    compaign_id: int,
    updated: AdCompaignPartialUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    compaign = db.query(AdCompaign).filter(AdCompaign.id == compaign_id).first()
    if not compaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    for field, value in updated.dict(exclude_unset=True).items():
        setattr(compaign, field, value)

    db.commit()
    db.refresh(compaign)
    return compaign

@router.put("/{compaign_id}", response_model=AdCompaignOut)
def update_adcompaign(
    compaign_id: int,
    updated: AdCompaignUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    compaign = db.query(AdCompaign).filter(AdCompaign.id == compaign_id).first()
    if not compaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    for field, value in updated.dict(exclude_unset=True).items():
        setattr(compaign, field, value)

    db.commit()
    db.refresh(compaign)
    return compaign

@router.delete("/{compaign_id}")
def delete_adcompaign(
    compaign_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    compaign = db.query(AdCompaign).filter(AdCompaign.id == compaign_id).first()
    if not compaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    db.delete(compaign)
    db.commit()
    return {"message": "Campaign deleted"}
