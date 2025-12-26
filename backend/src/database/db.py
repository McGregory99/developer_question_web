from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from sqlalchemy.util import quoted_token_parser
from . import models

def get_challenge_quota(db: Session, user_id: str):
    return db.query(models.ChallengeQuota).filter(models.ChallengeQuota.user_id == user_id).first()

def create_challenge_quota(db: Session, user_id: str):
    db_quota = models.ChallengeQuota(user_id=user_id)
    db.add(db_quota)
    db.commit()
    db.refresh(db_quota)
    return db_quota
        
def update_challenge_quota(db: Session, user_id: str, quota_remaining: int) -> models.ChallengeQuota:
    challenge_quota = get_challenge_quota(db, user_id)
    challenge_quota.quota_remaining = quota_remaining
    db.commit()
    db.refresh(challenge_quota)
    return challenge_quota

def reset_quota_if_needed(db: Session, quota: models.ChallengeQuota):
    now = datetime.now()
    if now - quota.last_reset_time > timedelta(hours=24):
        quota.remaining_quota = 10
        quota.last_reset_time = now
        db.commit()
        db.refresh(quota)
        return quota
    return quota

def create_challenge(
    db: Session, 
    difficulty: str, 
    created_by: str, 
    title: str, 
    options: str, 
    correct_answer_id: int, 
    explanation: str
):
    db_challenge = models.Challenge(
        difficulty=difficulty,
        created_by=created_by,
        title=title,
        options=options,
        correct_answer_id=correct_answer_id,
        explanation=explanation)
    db.add(db_challenge)
    db.commit()
    db.refresh(db_challenge)
    return db_challenge