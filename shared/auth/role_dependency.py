from fastapi import Depends, HTTPException

from shared.auth.auth_dependency import get_current_user


def admin_required(payload=Depends(get_current_user)):

    if payload.get("role") != 1:
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return payload
def customer_required(payload=Depends(get_current_user)):

    if payload.get("role") != 2:
        raise HTTPException(
            status_code=403,
            detail="Customer access required"
        )

    return payload