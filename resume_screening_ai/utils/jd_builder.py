"""Canonical job description builder based on job title and experience."""
from __future__ import annotations

from typing import Dict, List

JOB_ROLE_CONFIG: Dict[str, Dict[str, object]] = {
    "frontend developer": {
        "required_skills": ["react", "javascript", "html", "css"],
        "optional_skills": ["typescript", "frontend", "ui", "ux"],
        "education": "bachelor",
    },
    "backend engineer": {
        "required_skills": ["python", "sql", "docker", "api"],
        "optional_skills": ["kubernetes", "cloud", "cicd"],
        "education": "bachelor",
    },
    "full stack engineer": {
        "required_skills": ["javascript", "react", "node", "sql"],
        "optional_skills": ["typescript", "docker", "cloud"],
        "education": "bachelor",
    },
    "data scientist": {
        "required_skills": ["python", "machine learning", "sql", "pandas"],
        "optional_skills": ["statistics", "deep learning", "nlp"],
        "education": "master",
    },
    "data engineer": {
        "required_skills": ["python", "sql", "spark", "airflow"],
        "optional_skills": ["kubernetes", "docker", "cloud"],
        "education": "bachelor",
    },
    "ml engineer": {
        "required_skills": ["python", "machine learning", "docker", "api"],
        "optional_skills": ["pytorch", "tensorflow", "kubernetes"],
        "education": "bachelor",
    },
    "devops engineer": {
        "required_skills": ["docker", "kubernetes", "cicd", "cloud"],
        "optional_skills": ["terraform", "ansible", "monitoring"],
        "education": "bachelor",
    },
    "mobile developer": {
        "required_skills": ["react", "javascript", "frontend"],
        "optional_skills": ["typescript", "ui", "ux"],
        "education": "bachelor",
    },
    "android developer": {
        "required_skills": ["kotlin", "java", "android"],
        "optional_skills": ["jetpack", "compose", "ui"],
        "education": "bachelor",
    },
    "ios developer": {
        "required_skills": ["swift", "ios", "ui"],
        "optional_skills": ["objective c", "swiftui"],
        "education": "bachelor",
    },
    "qa engineer": {
        "required_skills": ["testing", "automation", "api"],
        "optional_skills": ["selenium", "cypress", "pytest"],
        "education": "bachelor",
    },
    "product manager": {
        "required_skills": ["product", "roadmap", "analytics", "stakeholder"],
        "optional_skills": ["sql", "experimentation", "ui"],
        "education": "bachelor",
    },
    "cloud engineer": {
        "required_skills": ["cloud", "docker", "kubernetes", "cicd"],
        "optional_skills": ["terraform", "monitoring", "security"],
        "education": "bachelor",
    },
    "security engineer": {
        "required_skills": ["security", "cloud", "monitoring", "api"],
        "optional_skills": ["iam", "siem", "kubernetes"],
        "education": "bachelor",
    },
    "data analyst": {
        "required_skills": ["sql", "excel", "tableau", "analytics"],
        "optional_skills": ["python", "power bi", "statistics"],
        "education": "bachelor",
    },
    "business analyst": {
        "required_skills": ["requirements", "analytics", "stakeholder", "documentation"],
        "optional_skills": ["sql", "excel", "process"],
        "education": "bachelor",
    },
    "data architect": {
        "required_skills": ["sql", "data modeling", "etl", "cloud"],
        "optional_skills": ["spark", "snowflake", "governance"],
        "education": "bachelor",
    },
    "ml ops engineer": {
        "required_skills": ["docker", "kubernetes", "cicd", "ml"],
        "optional_skills": ["model serving", "monitoring", "feature store"],
        "education": "bachelor",
    },
    "site reliability engineer": {
        "required_skills": ["monitoring", "incident", "automation", "cloud"],
        "optional_skills": ["slo", "observability", "terraform"],
        "education": "bachelor",
    },
    "platform engineer": {
        "required_skills": ["kubernetes", "cicd", "terraform", "cloud"],
        "optional_skills": ["networking", "security", "monitoring"],
        "education": "bachelor",
    },
    "solutions architect": {
        "required_skills": ["architecture", "cloud", "api", "design"],
        "optional_skills": ["security", "cost", "governance"],
        "education": "bachelor",
    },
    "database administrator": {
        "required_skills": ["sql", "backup", "tuning", "security"],
        "optional_skills": ["cloud", "replication", "monitoring"],
        "education": "bachelor",
    },
    "etl developer": {
        "required_skills": ["etl", "sql", "pipelines", "data modeling"],
        "optional_skills": ["airflow", "spark", "cloud"],
        "education": "bachelor",
    },
    "bi developer": {
        "required_skills": ["power bi", "tableau", "sql", "dashboards"],
        "optional_skills": ["dax", "data modeling", "python"],
        "education": "bachelor",
    },
    "game developer": {
        "required_skills": ["c++", "unity", "graphics", "physics"],
        "optional_skills": ["c#", "shaders", "networking"],
        "education": "bachelor",
    },
    "blockchain developer": {
        "required_skills": ["solidity", "smart contracts", "security", "api"],
        "optional_skills": ["web3", "ethereum", "testing"],
        "education": "bachelor",
    },
    "vr ar developer": {
        "required_skills": ["unity", "c#", "graphics", "3d"],
        "optional_skills": ["interaction", "ux", "performance"],
        "education": "bachelor",
    },
    "technical writer": {
        "required_skills": ["documentation", "api", "editing", "communication"],
        "optional_skills": ["markdown", "diagrams", "testing"],
        "education": "bachelor",
    },
    "ui designer": {
        "required_skills": ["ui", "figma", "prototyping", "visual design"],
        "optional_skills": ["ux", "design systems", "illustration"],
        "education": "bachelor",
    },
    "ux researcher": {
        "required_skills": ["research", "interviews", "surveys", "usability"],
        "optional_skills": ["statistics", "analysis", "presentation"],
        "education": "bachelor",
    },
    "graphic designer": {
        "required_skills": ["photoshop", "illustrator", "visual design", "branding"],
        "optional_skills": ["figma", "indesign", "motion"],
        "education": "bachelor",
    },
    "marketing manager": {
        "required_skills": ["marketing", "campaigns", "analytics", "content"],
        "optional_skills": ["seo", "sem", "email"],
        "education": "bachelor",
    },
    "seo specialist": {
        "required_skills": ["seo", "keywords", "analytics", "content"],
        "optional_skills": ["sem", "html", "cms"],
        "education": "bachelor",
    },
    "content strategist": {
        "required_skills": ["content", "editing", "planning", "seo"],
        "optional_skills": ["analytics", "social", "email"],
        "education": "bachelor",
    },
    "sales manager": {
        "required_skills": ["sales", "pipeline", "negotiation", "forecast"],
        "optional_skills": ["crm", "presentation", "analytics"],
        "education": "bachelor",
    },
    "customer success manager": {
        "required_skills": ["customer", "support", "onboarding", "retention"],
        "optional_skills": ["analytics", "presentation", "training"],
        "education": "bachelor",
    },
    "hr generalist": {
        "required_skills": ["hr", "recruiting", "onboarding", "compliance"],
        "optional_skills": ["payroll", "benefits", "employee relations"],
        "education": "bachelor",
    },
    "talent acquisition": {
        "required_skills": ["recruiting", "sourcing", "screening", "stakeholder"],
        "optional_skills": ["branding", "ats", "offer negotiation"],
        "education": "bachelor",
    },
    "finance analyst": {
        "required_skills": ["excel", "finance", "modeling", "reporting"],
        "optional_skills": ["sql", "power bi", "forecast"],
        "education": "bachelor",
    },
    "accountant": {
        "required_skills": ["accounting", "reconciliation", "reporting", "tax"],
        "optional_skills": ["erp", "excel", "audit"],
        "education": "bachelor",
    },
    "operations manager": {
        "required_skills": ["operations", "process", "planning", "analytics"],
        "optional_skills": ["lean", "six sigma", "automation"],
        "education": "bachelor",
    },
    "project manager": {
        "required_skills": ["project", "planning", "risk", "stakeholder"],
        "optional_skills": ["agile", "scrum", "jira"],
        "education": "bachelor",
    },
    "product designer": {
        "required_skills": ["ux", "ui", "prototyping", "research"],
        "optional_skills": ["design systems", "figma", "analytics"],
        "education": "bachelor",
    },
    "customer support": {
        "required_skills": ["support", "communication", "troubleshooting", "tickets"],
        "optional_skills": ["product knowledge", "documentation", "escalation"],
        "education": "bachelor",
    },
    "legal counsel": {
        "required_skills": ["contracts", "compliance", "review", "negotiation"],
        "optional_skills": ["privacy", "ip", "regulatory"],
        "education": "bachelor",
    },
    "medical data analyst": {
        "required_skills": ["sql", "python", "healthcare", "analytics"],
        "optional_skills": ["biostatistics", "power bi", "reporting"],
        "education": "bachelor",
    },
    "biomedical engineer": {
        "required_skills": ["biology", "engineering", "testing", "documentation"],
        "optional_skills": ["python", "hardware", "quality"],
        "education": "bachelor",
    },
    "robotics engineer": {
        "required_skills": ["c++", "python", "control", "hardware"],
        "optional_skills": ["ros", "simulation", "perception"],
        "education": "bachelor",
    },
    "firmware engineer": {
        "required_skills": ["c", "embedded", "rtos", "debugging"],
        "optional_skills": ["c++", "hardware", "drivers"],
        "education": "bachelor",
    },
    "embedded systems engineer": {
        "required_skills": ["embedded", "c", "hardware", "rtos"],
        "optional_skills": ["c++", "linux", "drivers"],
        "education": "bachelor",
    },
    "systems engineer": {
        "required_skills": ["systems", "linux", "scripting", "networking"],
        "optional_skills": ["automation", "cloud", "monitoring"],
        "education": "bachelor",
    },
    "release manager": {
        "required_skills": ["release", "planning", "coordination", "risk"],
        "optional_skills": ["cicd", "documentation", "compliance"],
        "education": "bachelor",
    },
    "build engineer": {
        "required_skills": ["cicd", "build systems", "scripting", "version control"],
        "optional_skills": ["containers", "automation", "monitoring"],
        "education": "bachelor",
    },
    "automation engineer": {
        "required_skills": ["automation", "scripting", "testing", "api"],
        "optional_skills": ["selenium", "cicd", "monitoring"],
        "education": "bachelor",
    },
    "integration engineer": {
        "required_skills": ["integration", "api", "testing", "troubleshooting"],
        "optional_skills": ["python", "postman", "logging"],
        "education": "bachelor",
    },
    "api engineer": {
        "required_skills": ["api", "rest", "design", "testing"],
        "optional_skills": ["graphql", "security", "monitoring"],
        "education": "bachelor",
    },
    "performance engineer": {
        "required_skills": ["performance", "profiling", "load testing", "analysis"],
        "optional_skills": ["jmeter", "apm", "optimization"],
        "education": "bachelor",
    },
    "observability engineer": {
        "required_skills": ["monitoring", "logging", "metrics", "alerts"],
        "optional_skills": ["grafana", "prometheus", "tracing"],
        "education": "bachelor",
    },
    "computer vision engineer": {
        "required_skills": ["python", "cv", "deep learning", "opencv"],
        "optional_skills": ["pytorch", "tensorflow", "deployment"],
        "education": "bachelor",
    },
    "nlp engineer": {
        "required_skills": ["python", "nlp", "transformers", "text processing"],
        "optional_skills": ["pytorch", "spacy", "deployment"],
        "education": "bachelor",
    },
    "applied scientist": {
        "required_skills": ["python", "ml", "experimentation", "analysis"],
        "optional_skills": ["pytorch", "statistics", "production"],
        "education": "master",
    },
    "analytics engineer": {
        "required_skills": ["sql", "dbt", "data modeling", "etl"],
        "optional_skills": ["python", "airflow", "bi"],
        "education": "bachelor",
    },
    "statistician": {
        "required_skills": ["statistics", "modeling", "analysis", "experiment design"],
        "optional_skills": ["r", "python", "reporting"],
        "education": "master",
    },
    "quantitative analyst": {
        "required_skills": ["python", "statistics", "modeling", "finance"],
        "optional_skills": ["sql", "risk", "derivatives"],
        "education": "master",
    },
    "decision scientist": {
        "required_skills": ["sql", "experiment design", "causal inference", "analytics"],
        "optional_skills": ["python", "statistics", "product"],
        "education": "master",
    },
    "data product manager": {
        "required_skills": ["product", "data", "requirements", "analytics"],
        "optional_skills": ["sql", "experimentation", "stakeholder"],
        "education": "bachelor",
    },
    "machine learning researcher": {
        "required_skills": ["ml", "research", "experimentation", "prototyping"],
        "optional_skills": ["pytorch", "tensorflow", "publication"],
        "education": "master",
    },
    "service designer": {
        "required_skills": ["service design", "research", "journey mapping", "workshops"],
        "optional_skills": ["facilitation", "prototyping", "systems thinking"],
        "education": "bachelor",
    },
    "ux writer": {
        "required_skills": ["writing", "ux", "microcopy", "voice"],
        "optional_skills": ["content design", "research", "docs"],
        "education": "bachelor",
    },
    "instructional designer": {
        "required_skills": ["instructional design", "curriculum", "storyboarding", "lms"],
        "optional_skills": ["assessment", "e-learning", "video"],
        "education": "bachelor",
    },
    "growth marketing manager": {
        "required_skills": ["growth", "experimentation", "analytics", "funnels"],
        "optional_skills": ["sql", "product", "lifecycle"],
        "education": "bachelor",
    },
    "performance marketer": {
        "required_skills": ["ads", "campaigns", "analytics", "budget"],
        "optional_skills": ["sem", "paid social", "attribution"],
        "education": "bachelor",
    },
    "social media manager": {
        "required_skills": ["social", "content", "community", "analytics"],
        "optional_skills": ["ads", "creative", "scheduling"],
        "education": "bachelor",
    },
    "content marketing manager": {
        "required_skills": ["content", "strategy", "seo", "editing"],
        "optional_skills": ["social", "email", "analytics"],
        "education": "bachelor",
    },
    "product marketing manager": {
        "required_skills": ["product marketing", "go-to-market", "positioning", "messaging"],
        "optional_skills": ["sales enablement", "research", "content"],
        "education": "bachelor",
    },
    "brand manager": {
        "required_skills": ["brand", "campaigns", "creative", "guidelines"],
        "optional_skills": ["research", "advertising", "events"],
        "education": "bachelor",
    },
    "public relations manager": {
        "required_skills": ["pr", "media", "communications", "press"],
        "optional_skills": ["events", "crisis", "speaking"],
        "education": "bachelor",
    },
    "marketing analyst": {
        "required_skills": ["analytics", "dashboards", "attribution", "insights"],
        "optional_skills": ["sql", "python", "experimentation"],
        "education": "bachelor",
    },
    "lifecycle marketer": {
        "required_skills": ["lifecycle", "crm", "segmentation", "automation"],
        "optional_skills": ["email", "push", "journeys"],
        "education": "bachelor",
    },
    "email marketing specialist": {
        "required_skills": ["email", "crm", "segmentation", "copywriting"],
        "optional_skills": ["html", "automation", "deliverability"],
        "education": "bachelor",
    },
    "community manager": {
        "required_skills": ["community", "engagement", "moderation", "content"],
        "optional_skills": ["events", "support", "analytics"],
        "education": "bachelor",
    },
    "account executive": {
        "required_skills": ["sales", "prospecting", "negotiation", "closing"],
        "optional_skills": ["crm", "presentation", "forecasting"],
        "education": "bachelor",
    },
    "business development representative": {
        "required_skills": ["prospecting", "outreach", "qualification", "pipeline"],
        "optional_skills": ["crm", "cold calling", "email"],
        "education": "bachelor",
    },
    "sales operations analyst": {
        "required_skills": ["sales ops", "analytics", "crm", "process"],
        "optional_skills": ["forecasting", "automation", "reporting"],
        "education": "bachelor",
    },
    "sales engineer": {
        "required_skills": ["sales", "technical", "demos", "solutions"],
        "optional_skills": ["api", "cloud", "architecture"],
        "education": "bachelor",
    },
    "solutions consultant": {
        "required_skills": ["solutions", "requirements", "demos", "proposals"],
        "optional_skills": ["cloud", "architecture", "pricing"],
        "education": "bachelor",
    },
    "implementation specialist": {
        "required_skills": ["implementation", "training", "configuration", "support"],
        "optional_skills": ["project management", "documentation", "api"],
        "education": "bachelor",
    },
    "renewals manager": {
        "required_skills": ["renewals", "negotiation", "customer", "pipeline"],
        "optional_skills": ["forecast", "contracts", "risk"],
        "education": "bachelor",
    },
    "onboarding specialist": {
        "required_skills": ["onboarding", "training", "configuration", "support"],
        "optional_skills": ["documentation", "customer success", "process"],
        "education": "bachelor",
    },
    "support operations analyst": {
        "required_skills": ["support ops", "analytics", "process", "tooling"],
        "optional_skills": ["automation", "crm", "knowledge base"],
        "education": "bachelor",
    },
    "hr business partner": {
        "required_skills": ["hrbp", "coaching", "employee relations", "strategy"],
        "optional_skills": ["analytics", "org design", "planning"],
        "education": "bachelor",
    },
    "compensation analyst": {
        "required_skills": ["compensation", "benchmarking", "analytics", "modeling"],
        "optional_skills": ["equity", "hris", "compliance"],
        "education": "bachelor",
    },
    "learning and development specialist": {
        "required_skills": ["training", "curriculum", "facilitation", "assessment"],
        "optional_skills": ["lms", "content", "coaching"],
        "education": "bachelor",
    },
    "recruiter": {
        "required_skills": ["sourcing", "screening", "interviewing", "closing"],
        "optional_skills": ["ats", "branding", "coordination"],
        "education": "bachelor",
    },
    "people operations manager": {
        "required_skills": ["people ops", "process", "hris", "analytics"],
        "optional_skills": ["policy", "compliance", "automation"],
        "education": "bachelor",
    },
    "controller": {
        "required_skills": ["accounting", "close", "reporting", "compliance"],
        "optional_skills": ["erp", "audit", "tax"],
        "education": "bachelor",
    },
    "fp&a manager": {
        "required_skills": ["fp&a", "forecasting", "budgeting", "analysis"],
        "optional_skills": ["excel", "modeling", "dashboards"],
        "education": "bachelor",
    },
    "internal auditor": {
        "required_skills": ["audit", "controls", "risk", "testing"],
        "optional_skills": ["sox", "compliance", "reporting"],
        "education": "bachelor",
    },
    "treasury analyst": {
        "required_skills": ["treasury", "cash management", "forecasting", "banking"],
        "optional_skills": ["hedging", "risk", "reporting"],
        "education": "bachelor",
    },
    "procurement manager": {
        "required_skills": ["procurement", "negotiation", "vendors", "contracts"],
        "optional_skills": ["savings", "analytics", "compliance"],
        "education": "bachelor",
    },
    "program manager": {
        "required_skills": ["program", "planning", "risk", "stakeholder"],
        "optional_skills": ["roadmaps", "reporting", "agile"],
        "education": "bachelor",
    },
    "business operations manager": {
        "required_skills": ["operations", "strategy", "analytics", "process"],
        "optional_skills": ["sql", "experimentation", "automation"],
        "education": "bachelor",
    },
    "supply chain manager": {
        "required_skills": ["supply chain", "planning", "inventory", "vendors"],
        "optional_skills": ["logistics", "analytics", "erp"],
        "education": "bachelor",
    },
    "logistics coordinator": {
        "required_skills": ["logistics", "shipping", "tracking", "communication"],
        "optional_skills": ["inventory", "vendors", "excel"],
        "education": "bachelor",
    },
    "office manager": {
        "required_skills": ["office", "facilities", "vendors", "coordination"],
        "optional_skills": ["events", "budget", "supplies"],
        "education": "bachelor",
    },
    "compliance manager": {
        "required_skills": ["compliance", "policies", "audits", "risk"],
        "optional_skills": ["privacy", "training", "reporting"],
        "education": "bachelor",
    },
    "contract manager": {
        "required_skills": ["contracts", "negotiation", "redlining", "risk"],
        "optional_skills": ["procurement", "compliance", "vendor"],
        "education": "bachelor",
    },
    "paralegal": {
        "required_skills": ["legal research", "drafting", "filings", "documentation"],
        "optional_skills": ["contracts", "litigation", "compliance"],
        "education": "bachelor",
    },
    "risk manager": {
        "required_skills": ["risk", "assessment", "mitigation", "reporting"],
        "optional_skills": ["insurance", "compliance", "controls"],
        "education": "bachelor",
    },
    "clinical researcher": {
        "required_skills": ["research", "protocols", "data collection", "analysis"],
        "optional_skills": ["clinical trials", "regulatory", "reporting"],
        "education": "bachelor",
    },
    "healthcare administrator": {
        "required_skills": ["operations", "compliance", "billing", "scheduling"],
        "optional_skills": ["ehr", "reporting", "staffing"],
        "education": "bachelor",
    },
    "lab technician": {
        "required_skills": ["lab", "testing", "samples", "documentation"],
        "optional_skills": ["equipment", "quality", "safety"],
        "education": "bachelor",
    },
    "regulatory affairs specialist": {
        "required_skills": ["regulatory", "submission", "compliance", "documentation"],
        "optional_skills": ["quality", "clinical", "audits"],
        "education": "bachelor",
    },
    "pharmacist": {
        "required_skills": ["pharmacy", "dispensing", "counseling", "compliance"],
        "optional_skills": ["inventory", "insurance", "regulatory"],
        "education": "bachelor",
    },
    "mechanical engineer": {
        "required_skills": ["mechanical", "cad", "analysis", "prototyping"],
        "optional_skills": ["fea", "manufacturing", "testing"],
        "education": "bachelor",
    },
    "electrical engineer": {
        "required_skills": ["electrical", "circuit design", "testing", "schematics"],
        "optional_skills": ["pcb", "embedded", "simulation"],
        "education": "bachelor",
    },
    "electronics engineer": {
        "required_skills": ["electronics", "circuit design", "testing", "debugging"],
        "optional_skills": ["pcb", "embedded", "simulation"],
        "education": "bachelor",
    },
    "hardware engineer": {
        "required_skills": ["hardware", "schematics", "testing", "debugging"],
        "optional_skills": ["fpga", "pcb", "validation"],
        "education": "bachelor",
    },
    "manufacturing engineer": {
        "required_skills": ["manufacturing", "process", "quality", "lean"],
        "optional_skills": ["automation", "six sigma", "safety"],
        "education": "bachelor",
    },
    "maintenance engineer": {
        "required_skills": ["maintenance", "troubleshooting", "equipment", "safety"],
        "optional_skills": ["cmms", "planning", "root cause"],
        "education": "bachelor",
    },
    "quality assurance manager": {
        "required_skills": ["quality", "audits", "process", "compliance"],
        "optional_skills": ["iso", "six sigma", "training"],
        "education": "bachelor",
    },
    "field service engineer": {
        "required_skills": ["support", "maintenance", "troubleshooting", "customer"],
        "optional_skills": ["hardware", "documentation", "training"],
        "education": "bachelor",
    },
    "teacher": {
        "required_skills": ["teaching", "lesson planning", "assessment", "classroom"],
        "optional_skills": ["technology", "curriculum", "communication"],
        "education": "bachelor",
    },
    "trainer": {
        "required_skills": ["training", "facilitation", "curriculum", "coaching"],
        "optional_skills": ["lms", "content", "assessment"],
        "education": "bachelor",
    },
    "copywriter": {
        "required_skills": ["copywriting", "editing", "headlines", "campaigns"],
        "optional_skills": ["seo", "brand", "social"],
        "education": "bachelor",
    },
    "editor": {
        "required_skills": ["editing", "proofreading", "style", "fact-checking"],
        "optional_skills": ["content", "publishing", "seo"],
        "education": "bachelor",
    },
    "translator": {
        "required_skills": ["translation", "language", "editing", "localization"],
        "optional_skills": ["terminology", "proofreading", "quality"],
        "education": "bachelor",
    },
}


ROLE_CATEGORIES: Dict[str, List[str]] = {
    "Software & Platform": [
        "frontend developer",
        "backend engineer",
        "full stack engineer",
        "mobile developer",
        "android developer",
        "ios developer",
        "qa engineer",
        "automation engineer",
        "devops engineer",
        "site reliability engineer",
        "platform engineer",
        "cloud engineer",
        "security engineer",
        "blockchain developer",
        "game developer",
        "vr ar developer",
        "firmware engineer",
        "embedded systems engineer",
        "systems engineer",
        "release manager",
        "build engineer",
        "integration engineer",
        "api engineer",
        "performance engineer",
        "observability engineer",
        "solutions architect",
        "database administrator",
        "product manager",
        "project manager",
        "program manager",
    ],
    "Data & AI": [
        "data scientist",
        "data engineer",
        "data analyst",
        "business analyst",
        "data architect",
        "ml engineer",
        "ml ops engineer",
        "analytics engineer",
        "statistician",
        "quantitative analyst",
        "decision scientist",
        "applied scientist",
        "machine learning researcher",
        "computer vision engineer",
        "nlp engineer",
        "data product manager",
        "bi developer",
        "etl developer",
        "medical data analyst",
    ],
    "Product, Design & Content": [
        "product designer",
        "ui designer",
        "ux researcher",
        "graphic designer",
        "technical writer",
        "service designer",
        "ux writer",
        "instructional designer",
        "content strategist",
        "copywriter",
        "editor",
        "translator",
    ],
    "Marketing & Growth": [
        "marketing manager",
        "growth marketing manager",
        "performance marketer",
        "product marketing manager",
        "brand manager",
        "public relations manager",
        "seo specialist",
        "content marketing manager",
        "social media manager",
        "lifecycle marketer",
        "email marketing specialist",
        "marketing analyst",
        "community manager",
    ],
    "Sales & Customer": [
        "sales manager",
        "account executive",
        "business development representative",
        "sales operations analyst",
        "sales engineer",
        "solutions consultant",
        "implementation specialist",
        "renewals manager",
        "customer success manager",
        "customer support",
        "onboarding specialist",
        "support operations analyst",
    ],
    "People & HR": [
        "hr generalist",
        "talent acquisition",
        "recruiter",
        "hr business partner",
        "compensation analyst",
        "learning and development specialist",
        "people operations manager",
        "instructional designer",
        "trainer",
    ],
    "Finance & Legal": [
        "finance analyst",
        "accountant",
        "controller",
        "fp&a manager",
        "internal auditor",
        "treasury analyst",
        "procurement manager",
        "compliance manager",
        "contract manager",
        "paralegal",
        "legal counsel",
        "risk manager",
    ],
    "Operations & Supply": [
        "operations manager",
        "project manager",
        "program manager",
        "business operations manager",
        "supply chain manager",
        "logistics coordinator",
        "office manager",
    ],
    "Hardware & Manufacturing": [
        "firmware engineer",
        "embedded systems engineer",
        "systems engineer",
        "mechanical engineer",
        "electrical engineer",
        "electronics engineer",
        "hardware engineer",
        "manufacturing engineer",
        "maintenance engineer",
        "quality assurance manager",
        "field service engineer",
        "robotics engineer",
        "biomedical engineer",
    ],
    "Healthcare & Science": [
        "medical data analyst",
        "clinical researcher",
        "healthcare administrator",
        "lab technician",
        "regulatory affairs specialist",
        "pharmacist",
        "biomedical engineer",
    ],
    "Education & Community": [
        "teacher",
        "trainer",
        "instructional designer",
        "technical writer",
        "community manager",
    ],
}


def _adjust_by_experience(required: List[str], optional: List[str], experience_years: int) -> List[str]:
    if experience_years < 2:
        return required[: max(1, len(required) // 2)]
    if experience_years < 5:
        return required
    # senior: include a couple of optional skills as expectations
    extras = optional[:2] if optional else []
    return list(dict.fromkeys(required + extras))


def build_jd(job_title: str, experience_years: int) -> Dict[str, object]:
    normalized_title = job_title.lower().strip()
    config = JOB_ROLE_CONFIG.get(normalized_title, JOB_ROLE_CONFIG["frontend developer"])

    required_skills = _adjust_by_experience(
        config.get("required_skills", []),
        config.get("optional_skills", []),
        experience_years,
    )
    optional_skills = list(config.get("optional_skills", []))
    min_experience = max(0, experience_years)
    education_preference = config.get("education", "bachelor")

    description_lines = [
        f"Role: {normalized_title.title()}",
        f"Minimum experience: {min_experience} years",
        f"Education preference: {education_preference}",
        f"Required skills: {', '.join(required_skills)}",
    ]
    if optional_skills:
        description_lines.append(f"Optional skills: {', '.join(optional_skills)}")

    jd_text = "\n".join(description_lines)

    return {
        "job_title": normalized_title,
        "required_skills": required_skills,
        "optional_skills": optional_skills,
        "min_experience": min_experience,
        "education_preference": education_preference,
        "description": jd_text,
    }
