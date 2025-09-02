from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.agent_schema import AgentCreate, AgentUpdate, AgentOut
from services import agent_service

router = APIRouter(prefix="/agents", tags=["Agents"])

@router.post("/", response_model=AgentOut)
def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    return agent_service.create_agent(db, agent)

@router.get("/{agent_id}", response_model=AgentOut)
def read_agent(agent_id: int, db: Session = Depends(get_db)):
    db_agent = agent_service.get_agent(db, agent_id)
    if not db_agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent

@router.get("/", response_model=list[AgentOut])
def read_agents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return agent_service.get_agents(db, skip, limit)

@router.put("/{agent_id}", response_model=AgentOut)
def update_agent(agent_id: int, agent: AgentUpdate, db: Session = Depends(get_db)):
    return agent_service.update_agent(db, agent_id, agent)

@router.delete("/{agent_id}", response_model=AgentOut)
def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    return agent_service.delete_agent(db, agent_id)




