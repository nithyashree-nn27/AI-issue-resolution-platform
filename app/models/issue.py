from pydantic import BaseModel, Field


class IssueRequest(BaseModel):
    """Request payload for issue resolution."""

    query: str = Field(
        ...,
        min_length=3,
        max_length=1000,
        description="Support issue submitted by the user",
        examples=["My refund is still pending"],
    )

    user_role: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Role of the requesting user",
        examples=["support"],
    )

    order_id: str | None = Field(
        default=None,
        max_length=100,
        description="Optional order identifier",
        examples=["ORD-12345"],
    )


class IssueResponse(BaseModel):
    """Standard response returned by the issue-resolution service."""

    status: str
    category: str
    message: str
    source: str