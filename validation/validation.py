from fastapi import HTTPException, Request


async def validate_score(request: Request):
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Введите значение оценки от 1 до 5"
        )

    if 'score' not in body:
        raise HTTPException(
            status_code=400,
            detail="Введите значение оценки от 1 до 5"
        )

    score = body['score']
    if not isinstance(score, int):
        raise HTTPException(
            status_code=400,
            detail="Введите значение оценки от 1 до 5"
        )

    if score < 1 or score > 5:
        raise HTTPException(
            status_code=400,
            detail="Введите значение оценки от 1 до 5"
        )
