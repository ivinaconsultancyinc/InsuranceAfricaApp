from fastapi import FastAPI
from .routers import client, policy
from .database import Base, engine
from .routers import client_router, policy_router, claims_loans
from .routers import product
from .routers import reinsurance
from .routers import commissions
from routers import gl
from models.gl_model import Base as GLBase
from routers import dashboard
from fastapi.middleware.cors import CORSMiddleware
from auth import auth_router
from routers import accounts_payable 
from routers import statistical_reporting
from routers import audit_access
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routers import user
from routers import agent
from routers import customer
from routers import premium
from routers import document
from routers import ledger 
from routers import currency_converter 
from jwt_handler import create_token, decode_token
from routers.accounts_payable import router as accounts_payable_router
from routers.agent_router import router as agent_router
from routers.audit_access_router import router as audit_access_router
from routers.claims_loans_router import router as claims_loans_router
from routers.commissions_router import router as commissions_router
from routers.customer_router import router as customer_router
from routers.document_router import router as document_router
from routers.gl_router import router as gl_router
from routers.ledger_router import router as ledger_router
from routers.policy_router import router as policy_router
from routers.premium_router import router as premium_router
from routers.product_router import router as product_router
from routers.receivable_router import router as receivable_router
from routers.reinsurance_router import router as reinsurance_router
from routers.client_router import router as client_router
from routers.statistical_reporting_router import router as statistical_reporting_router
from routers.user_router import router as user_router





Base.metadata.create_all(bind=engine)
GLBase.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")


app = FastAPI()

app.include_router(client.router)
app.include_router(policy.router)
app.include_router(claims_loans.router)
app.include_router(product.router)
app.include_router(reinsurance.router)
app.include_router(commissions.router)
app.include_router(gl.router)
app.include_router(dashboard.router)
app.include_router(auth_router.router)
app.include_router(accounts_payable.router, prefix="/accounts-payable", tags=["Accounts Payable"])
app.include_router(statistical_reporting.router, prefix="/statistical-reporting", tags=["Statistical Reporting"])
app.include_router(audit_access.router, prefix="/audit-access", tags=["Audit & Access Control"])
app.include_router(ledger.router)
app.include_router(user.router)
app.include_router(agent.router)
app.include_router(customer.router)
app.include_router(premium.router)
app.include_router(document.router)
app.include_router(currency_converter.router, prefix="/currency", tags=["Currency Converter"])
app.include_router(accounts_payable_router, prefix="/accounts-payable", tags=["Accounts Payable"])
app.include_router(agent_router, prefix="/api", tags=["Agents"])
app.include_router(audit_access_router, prefix="/api/auditaccess", tags=["Audit Access"])
app.include_router(claims_loans_router, prefix="/api/claimsloans", tags=["Claims & Loans"])
app.include_router(commissions_router, prefix="/api/commissions", tags=["Commissions"])
app.include_router(customer_router, prefix="/api/customer", tags=["Customer"])
app.include_router(document_router, prefix="/api/document", tags=["Document"])
app.include_router(gl_router, prefix="/api/gl", tags=["General Ledger
app.include_router(ledger_router, prefix="/api/ledger", tags=["Ledger"])
app.include_router(policy_router, prefix="/api/policy", tags=["Policy"])
app.include_router(premium_router, prefix="/api/premium", tags=["Premium"])
app.include_router(client_router, prefix="/api/client", tags=["Client"])
app.include_router(statistical_reporting_router, prefix="/api/statisticalreport", tags=["Statistical Report"])
app.include_router(user_router, prefix="/api/user", tags=["User"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/audit/logs")
def view_logs(user: UserAccess = Depends(require_permission("view_logs"))):
    ...















