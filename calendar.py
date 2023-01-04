from fastapi import FastAPI


@app.post("/event")
def create_event(event: Event):
    # save event to database
    return {"event_id": event.id}

@app.get("/event/{event_id}")
def get_event(event_id: int):
    # retrieve event from database
    return event

@app.put("/event/{event_id}")
def update_event(event_id: int, event: Event):
    # update event in database
    return {"success": True}

@app.delete("/event/{event_id}")
def delete_event(event_id: int):
    # delete event from database
    return {"success": True}