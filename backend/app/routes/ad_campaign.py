from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.deps import get_db
from database.models import AdCampaign
from database.schemas import AdCampaignCreate, AdCampaignOut, AdCampaignUpdate, AdCampaignPartialUpdate
from auth.auth import get_current_user

router = APIRouter(prefix="/adcampaigns", tags=["AdCampaigns"])

@router.post("/", response_model=AdCampaignOut)
def create_adcampaign(
    campaign: AdCampaignCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    db_campaign = AdCampaign(**campaign.dict())
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign

@router.get("/", response_model=list[AdCampaignOut])
def list_adcampaigns(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return db.query(AdCampaign).all()

@router.get("/{campaign_id}", response_model=AdCampaignOut)
def get_adcampaign(
    campaign_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    campaign = db.query(AdCampaign).filter(AdCampaign.id == campaign_id).first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign

@router.patch("/{campaign_id}", response_model=AdCampaignOut)
def patch_adcampaign(
    campaign_id: int,
    updated: AdCampaignPartialUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    campaign = db.query(AdCampaign).filter(AdCampaign.id == campaign_id).first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    for field, value in updated.dict(exclude_unset=True).items():
        setattr(campaign, field, value)

    db.commit()
    db.refresh(campaign)
    return campaign

@router.put("/{campaign_id}", response_model=AdCampaignOut)
def update_adcampaign(
    campaign_id: int,
    updated: AdCampaignUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    campaign = db.query(AdCampaign).filter(AdCampaign.id == campaign_id).first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    for field, value in updated.dict(exclude_unset=True).items():
        setattr(campaign, field, value)

    db.commit()
    db.refresh(campaign)
    return campaign

@router.delete("/{campaign_id}")
def delete_adcampaign(
    campaign_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    campaign = db.query(AdCampaign).filter(AdCampaign.id == campaign_id).first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    db.delete(campaign)
    db.commit()
    return {"message": "Campaign deleted"}
