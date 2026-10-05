import logging

from fastapi import APIRouter, HTTPException

from app.models.issue import IssueRequest, IssueResponse
from app.services.authorization import is_authorized
from app.services.issue_resolution import resolve_issue


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1",
    tags=["Issue Resolution"],
)


@router.post(
    "/resolve",
    response_model=IssueResponse,
    summary="Resolve a support issue",
    description=(
        "Classify a support issue, retrieve relevant knowledge, "
        "and return a contextual resolution."
    ),
)
def resolve(request: IssueRequest) -> IssueResponse:

    logger.info(
        "Issue-resolution request received: role=%s, has_order_id=%s",
        request.user_role,
        bool(request.order_id),
    )

    if not is_authorized(request.user_role):
        logger.warning(
            "Unauthorized issue-resolution request: role=%s",
            request.user_role,
        )

        raise HTTPException(
            status_code=403,
            detail="User is not authorized to access issue-resolution services.",
        )

    result = resolve_issue(request.query)

    logger.info(
        "Issue-resolution completed: category=%s, status=%s",
        result["category"],
        result["status"],
    )

    return IssueResponse(**result)