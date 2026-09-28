# Comprehensive skill taxonomy and normalization dictionary for Smart CareerHub AI Engine

SKILL_TAXONOMY = {
    "Software & Web": [
        "React", "React.js", "Vue", "Vue.js", "Angular", "Next.js", "Nuxt.js",
        "HTML", "HTML5", "CSS", "CSS3", "Tailwind CSS", "Bootstrap", "Sass", "LESS",
        "JavaScript", "TypeScript", "Redux", "Zustand", "Webpack", "Vite", "Responsive Design",
        "Node.js", "Express", "Express.js", "NestJS", "Python", "Django", "FastAPI",
        "Flask", "Java", "Spring Boot", "C#", ".NET", "Go", "Golang", "PHP", "Laravel",
        "Ruby", "Ruby on Rails", "REST API", "GraphQL", "Microservices", "gRPC", "C++", "C"
    ],
    "Database": [
        "MongoDB", "PostgreSQL", "MySQL", "SQLite", "Redis", "Cassandra", "DynamoDB",
        "Firebase", "Supabase", "Oracle", "SQL", "NoSQL", "Prisma", "Mongoose", "Sequelize"
    ],
    "Cloud & DevOps": [
        "AWS", "Amazon Web Services", "Azure", "GCP", "Google Cloud", "Docker",
        "Kubernetes", "CI/CD", "GitHub Actions", "Jenkins", "Terraform", "Ansible",
        "Nginx", "Linux", "Bash", "Shell", "Serverless"
    ],
    "Data Science & Analytics": [
        "Python", "R", "Pandas", "NumPy", "Scikit-Learn", "TensorFlow", "PyTorch",
        "Keras", "OpenCV", "NLP", "Natural Language Processing", "Machine Learning",
        "Deep Learning", "Data Analysis", "Data Visualization", "PowerBI", "Power BI", "Tableau",
        "Spark", "Hadoop", "SQL", "Excel", "Data Mining", "Statistics"
    ],
    "Design & Graphics": [
        "Figma", "Adobe XD", "Sketch", "Photoshop", "Illustrator", "InDesign",
        "UI Design", "UX Design", "Wireframing", "Prototyping", "User Research",
        "Graphic Design", "Design Systems", "User Testing", "Visual Design"
    ],
    "Cybersecurity": [
        "Cybersecurity", "Penetration Testing", "Ethical Hacking", "Network Security",
        "Wireshark", "Metasploit", "SIEM", "Firewalls", "Cryptography", "Identity Management"
    ],
    "Digital Marketing & Sales": [
        "SEO", "Search Engine Optimization", "SEM", "Google Ads", "Content Marketing",
        "Social Media Marketing", "Email Marketing", "Google Analytics", "Copywriting",
        "CRM", "HubSpot", "Salesforce", "Lead Generation"
    ],
    "Finance & Business": [
        "Financial Analysis", "Accounting", "Excel", "Corporate Finance", "Financial Modeling",
        "Risk Assessment", "Taxation", "Auditing", "Budgeting", "Business Strategy",
        "Business Analysis", "Requirements Gathering"
    ],
    "HR & Management": [
        "Talent Acquisition", "Recruitment", "Employee Relations", "Performance Management",
        "HR Operations", "Payroll", "Onboarding", "Labor Laws", "HRIS"
    ],
    "QA & Testing": [
        "Manual Testing", "Automation Testing", "Selenium", "Jest", "Cypress", "Junit",
        "Postman", "QA", "Bug Tracking", "Test Cases", "Regression Testing"
    ],
    "Tools & Workflow": [
        "Git", "GitHub", "GitLab", "Bitbucket", "Jira", "Postman", "Swagger",
        "VS Code", "Trello", "Agile", "Scrum"
    ],
    "Soft Skills": [
        "Communication", "Teamwork", "Problem Solving", "Critical Thinking",
        "Leadership", "Time Management", "Adaptability", "Collaboration", "Analytical Skills"
    ]
}

# Skill Normalization Map (Synonyms -> Standard Display Form)
SKILL_SYNONYMS = {
    "reactjs": "React",
    "react.js": "React",
    "react": "React",
    "nodejs": "Node.js",
    "node.js": "Node.js",
    "node": "Node.js",
    "expressjs": "Express.js",
    "express.js": "Express.js",
    "express": "Express.js",
    "mongodb": "MongoDB",
    "mongo db": "MongoDB",
    "mongo": "MongoDB",
    "js": "JavaScript",
    "javascript": "JavaScript",
    "ts": "TypeScript",
    "typescript": "TypeScript",
    "aws": "AWS",
    "amazon web services": "AWS",
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",
    "py": "Python",
    "python": "Python",
    "powerbi": "Power BI",
    "power bi": "Power BI",
    "html": "HTML",
    "html5": "HTML",
    "css": "CSS",
    "css3": "CSS",
    "ui/ux": "UI/UX Design",
    "figma": "Figma",
    "photoshop": "Photoshop",
    "illustrator": "Illustrator",
    "seo": "SEO",
    "qa": "QA / Testing"
}

ROLE_REQUIREMENTS = {
    "MERN Developer": {
        "required": ["JavaScript", "React", "Node.js", "Express.js", "MongoDB", "HTML", "CSS", "Git"],
        "preferred": ["TypeScript", "Docker", "AWS", "Next.js", "Redux", "Tailwind CSS", "REST API"],
        "min_experience_years": 0
    },
    "Java Developer": {
        "required": ["Java", "Spring Boot", "SQL", "Git", "REST API"],
        "preferred": ["Microservices", "Docker", "PostgreSQL", "Maven", "JUnit", "AWS"],
        "min_experience_years": 0
    },
    "Python Developer": {
        "required": ["Python", "Django", "FastAPI", "SQL", "Git", "REST API"],
        "preferred": ["Docker", "PostgreSQL", "Redis", "Celery", "AWS"],
        "min_experience_years": 0
    },
    "Software Engineer": {
        "required": ["Data Structures", "Algorithms", "Java", "Python", "SQL", "Git"],
        "preferred": ["Docker", "AWS", "System Design", "CI/CD", "Linux"],
        "min_experience_years": 0
    },
    "Data Analyst": {
        "required": ["Python", "SQL", "Pandas", "Excel", "Data Analysis"],
        "preferred": ["Power BI", "Tableau", "NumPy", "Scikit-Learn", "Data Visualization"],
        "min_experience_years": 0
    },
    "Data Scientist": {
        "required": ["Python", "Machine Learning", "SQL", "Pandas", "NumPy", "Statistics"],
        "preferred": ["PyTorch", "TensorFlow", "Deep Learning", "NLP", "Scikit-Learn"],
        "min_experience_years": 0
    },
    "UI/UX Designer": {
        "required": ["Figma", "Wireframing", "Prototyping", "User Research", "UI Design"],
        "preferred": ["HTML", "CSS", "Adobe XD", "User Testing", "Design Systems"],
        "min_experience_years": 0
    },
    "Graphic Designer": {
        "required": ["Photoshop", "Illustrator", "Graphic Design", "Typography", "Figma"],
        "preferred": ["InDesign", "Branding", "UI Design", "Visual Design"],
        "min_experience_years": 0
    },
    "Cloud Engineer": {
        "required": ["AWS", "Docker", "Linux", "Networking", "Git"],
        "preferred": ["Kubernetes", "Azure", "Terraform", "Python", "CI/CD"],
        "min_experience_years": 0
    },
    "Cybersecurity Analyst": {
        "required": ["Cybersecurity", "Network Security", "Linux", "Firewalls", "Wireshark"],
        "preferred": ["Penetration Testing", "SIEM", "Ethical Hacking", "Python", "Cryptography"],
        "min_experience_years": 0
    },
    "Digital Marketing": {
        "required": ["SEO", "Google Ads", "Social Media Marketing", "Content Marketing", "Google Analytics"],
        "preferred": ["Copywriting", "Email Marketing", "CRM", "HubSpot", "SEM"],
        "min_experience_years": 0
    },
    "Business Analyst": {
        "required": ["Business Analysis", "Requirements Gathering", "SQL", "Excel", "Communication"],
        "preferred": ["Power BI", "Jira", "Agile", "Process Mapping", "Tableau"],
        "min_experience_years": 0
    },
    "QA / Testing Engineer": {
        "required": ["Manual Testing", "Test Cases", "Bug Tracking", "SQL", "Git"],
        "preferred": ["Automation Testing", "Selenium", "Jest", "Postman", "Cypress"],
        "min_experience_years": 0
    },
    "HR Specialist": {
        "required": ["Talent Acquisition", "Recruitment", "Employee Relations", "Communication", "HR Operations"],
        "preferred": ["HRIS", "Payroll", "Performance Management", "Labor Laws"],
        "min_experience_years": 0
    },
    "Finance Analyst": {
        "required": ["Financial Analysis", "Excel", "Accounting", "Financial Modeling", "Corporate Finance"],
        "preferred": ["Risk Assessment", "SQL", "Budgeting", "Power BI", "Auditing"],
        "min_experience_years": 0
    }
}
