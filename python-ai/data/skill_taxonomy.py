# Comprehensive skill taxonomy and role benchmark matrix for Smart CareerHub AI Engine

SKILL_TAXONOMY = {
    "Frontend": [
        "React", "React.js", "Vue", "Vue.js", "Angular", "Next.js", "Nuxt.js",
        "HTML", "HTML5", "CSS", "CSS3", "Tailwind CSS", "Bootstrap", "Sass", "LESS",
        "JavaScript", "TypeScript", "Redux", "Zustand", "Webpack", "Vite", "Responsive Design"
    ],
    "Backend": [
        "Node.js", "Express", "Express.js", "NestJS", "Python", "Django", "FastAPI",
        "Flask", "Java", "Spring Boot", "C#", ".NET", "Go", "Golang", "PHP", "Laravel",
        "Ruby", "Ruby on Rails", "REST API", "GraphQL", "Microservices", "gRPC"
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
    "Data & AI": [
        "Python", "R", "Pandas", "NumPy", "Scikit-Learn", "TensorFlow", "PyTorch",
        "Keras", "OpenCV", "NLP", "Natural Language Processing", "Machine Learning",
        "Deep Learning", "Data Analysis", "Data Visualization", "PowerBI", "Tableau",
        "Spark", "Hadoop", "SQL", "LLMs", "LangChain"
    ],
    "Tools & Workflow": [
        "Git", "GitHub", "GitLab", "Bitbucket", "Jira", "Postman", "Swagger",
        "VS Code", "Figma", "Trello", "Agile", "Scrum"
    ],
    "Mobile": [
        "React Native", "Flutter", "Swift", "Kotlin", "Android", "iOS", "Dart"
    ],
    "Soft Skills": [
        "Communication", "Teamwork", "Problem Solving", "Critical Thinking",
        "Leadership", "Time Management", "Adaptability", "Collaboration", "Analytical Skills"
    ]
}

ROLE_REQUIREMENTS = {
    "Full Stack Developer": {
        "required": ["JavaScript", "React", "Node.js", "Express", "MongoDB", "HTML", "CSS", "Git"],
        "preferred": ["TypeScript", "Docker", "AWS", "Next.js", "Redux", "Tailwind CSS", "REST API"],
        "min_experience_years": 0
    },
    "Frontend Developer": {
        "required": ["JavaScript", "React", "HTML", "CSS", "Tailwind CSS", "Git"],
        "preferred": ["TypeScript", "Next.js", "Redux", "Vite", "Responsive Design"],
        "min_experience_years": 0
    },
    "Backend Developer": {
        "required": ["Node.js", "Express", "MongoDB", "SQL", "REST API", "Git"],
        "preferred": ["Python", "Docker", "AWS", "Redis", "TypeScript", "Microservices"],
        "min_experience_years": 0
    },
    "Python AI Engineer": {
        "required": ["Python", "FastAPI", "Machine Learning", "NLP", "Pandas", "Git"],
        "preferred": ["PyTorch", "TensorFlow", "Docker", "AWS", "Scikit-Learn", "LLMs"],
        "min_experience_years": 0
    },
    "DevOps Engineer": {
        "required": ["Docker", "Kubernetes", "AWS", "Linux", "CI/CD", "Git"],
        "preferred": ["Terraform", "Ansible", "Python", "Nginx", "GitHub Actions"],
        "min_experience_years": 0
    },
    "Data Analyst": {
        "required": ["Python", "SQL", "Pandas", "Data Analysis", "Excel"],
        "preferred": ["PowerBI", "Tableau", "NumPy", "Scikit-Learn", "Data Visualization"],
        "min_experience_years": 0
    },
    "Cloud Engineer": {
        "required": ["AWS", "Docker", "Linux", "Networking", "Git"],
        "preferred": ["Kubernetes", "Azure", "Terraform", "Python", "CI/CD"],
        "min_experience_years": 0
    },
    "UI/UX Designer": {
        "required": ["Figma", "Wireframing", "Prototyping", "User Research", "UI Design"],
        "preferred": ["HTML", "CSS", "Adobe XD", "User Testing", "Design Systems"],
        "min_experience_years": 0
    }
}
