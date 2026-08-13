"""
Mock data repositories, skill taxonomies, role matrix, and realistic question banks for CareerAI.
"""

ROLE_TAXONOMY = {
    "Software Developer": {
        "title": "Software Developer",
        "category": "Core Engineering",
        "description": "Designs, builds, and maintains robust software systems, algorithms, APIs, and scalable software architectures.",
        "core_skills": [
            {"name": "Data Structures & Algorithms", "importance": "High", "weight": 25},
            {"name": "Python / Java / C++", "importance": "High", "weight": 20},
            {"name": "Object-Oriented Programming (OOP)", "importance": "High", "weight": 15},
            {"name": "Git & Version Control", "importance": "Medium", "weight": 10},
            {"name": "SQL & Relational Databases", "importance": "High", "weight": 15},
            {"name": "RESTful API Design", "importance": "Medium", "weight": 10},
            {"name": "System Design Basics", "importance": "Medium", "weight": 5}
        ],
        "recommended_projects": [
            "Full-Stack Web App with REST API & SQLite/Postgres",
            "Multi-threaded Task Queue or Cache System",
            "Algorithmic Data Analyzer with Visual Benchmarks"
        ],
        "interview_topics": [
            "Time & Space Complexity Analysis",
            "OOP Principles (Encapsulation, Polymorphism, Inheritance, Abstraction)",
            "Database Indexing, Normalization & ACID Transactions",
            "API Authentication (JWT/OAuth) and Error Handling",
            "Concurrency, Threads, and Process Management"
        ]
    },
    "Python Developer": {
        "title": "Python Developer",
        "category": "Software Engineering",
        "description": "Specializes in developing backend services, automation scripts, data pipelines, and web applications using Python ecosystem.",
        "core_skills": [
            {"name": "Python (Advanced OOP & Metaprogramming)", "importance": "High", "weight": 25},
            {"name": "Flask / FastAPI / Django", "importance": "High", "weight": 20},
            {"name": "SQL & ORMs (SQLAlchemy)", "importance": "High", "weight": 15},
            {"name": "Asyncio & Multiprocessing", "importance": "Medium", "weight": 15},
            {"name": "Unit Testing & Pytest", "importance": "Medium", "weight": 10},
            {"name": "Git & CI/CD", "importance": "Medium", "weight": 10},
            {"name": "Docker Basics", "importance": "Low", "weight": 5}
        ],
        "recommended_projects": [
            "Microservice REST API with Flask/FastAPI & Token Authentication",
            "Automated Web Scraping and Data Pipeline with Celery",
            "Facial Recognition or OpenCV Vision Processing Service"
        ],
        "interview_topics": [
            "Python Memory Management & Global Interpreter Lock (GIL)",
            "Generators, Iterators, and List Comprehensions",
            "Decorators, Context Managers (`with` statement), and Dunder methods",
            "Flask vs Django architectural trade-offs",
            "Database Connection Pooling & Query Optimization"
        ]
    },
    "Web Developer": {
        "title": "Web Developer",
        "category": "Frontend & Full Stack",
        "description": "Builds responsive, high-performance web interfaces and connects them with scalable backend services.",
        "core_skills": [
            {"name": "HTML5 & Modern CSS3 (Flexbox/Grid)", "importance": "High", "weight": 20},
            {"name": "JavaScript (ES6+) & DOM APIs", "importance": "High", "weight": 25},
            {"name": "Responsive Design & Mobile-First UX", "importance": "High", "weight": 15},
            {"name": "Backend Integration (Flask/Node.js)", "importance": "High", "weight": 15},
            {"name": "REST APIs & Fetch/Axios", "importance": "High", "weight": 10},
            {"name": "Web Performance & Accessibility (a11y)", "importance": "Medium", "weight": 10},
            {"name": "Git & Deployment", "importance": "Low", "weight": 5}
        ],
        "recommended_projects": [
            "Dynamic SaaS Dashboard with Dark/Light Themes and Glassmorphism",
            "E-Commerce Cart or Booking Engine with Real-Time Validation",
            "Interactive Single Page Application (SPA) with Flask REST Backend"
        ],
        "interview_topics": [
            "CSS Box Model, Flexbox vs CSS Grid, and Media Queries",
            "JavaScript Event Loop, Closures, Promises, and Async/Await",
            "Browser Rendering Lifecycle and DOM Manipulation Performance",
            "Cross-Origin Resource Sharing (CORS) & Security Headers",
            "Progressive Enhancement and Semantic Web Standards"
        ]
    },
    "Data Analyst": {
        "title": "Data Analyst",
        "category": "Data & Analytics",
        "description": "Transforms raw telemetry, business records, and metrics into actionable insights, dashboards, and reports.",
        "core_skills": [
            {"name": "SQL (Complex Joins, Aggregations, Window Functions)", "importance": "High", "weight": 30},
            {"name": "Python (Pandas, NumPy)", "importance": "High", "weight": 25},
            {"name": "Data Visualization (Matplotlib, Seaborn, PowerBI)", "importance": "High", "weight": 15},
            {"name": "Exploratory Data Analysis (EDA)", "importance": "High", "weight": 15},
            {"name": "Statistical Analysis & Probability", "importance": "Medium", "weight": 10},
            {"name": "Excel / Google Sheets Advanced", "importance": "Low", "weight": 5}
        ],
        "recommended_projects": [
            "End-to-End Sales & Churn Analytics Dashboard with Python & SQL",
            "IoT Environmental Sensor Trend and Outlier Analysis",
            "Customer Segmentation Analysis with Clustering Visualization"
        ],
        "interview_topics": [
            "SQL Window Functions (ROW_NUMBER, RANK, LEAD, LAG)",
            "Handling Missing Values, Outliers, and Data Imputation",
            "Correlation vs Causation and Hypothesis Testing",
            "Data Storytelling and Executive KPI Presentation",
            "ETL Pipelines and Data Cleansing Strategies"
        ]
    },
    "AI/ML Beginner": {
        "title": "AI/ML Engineer (Foundations)",
        "category": "Artificial Intelligence",
        "description": "Applies machine learning algorithms, computer vision models, and natural language processing to automate cognitive tasks.",
        "core_skills": [
            {"name": "Python for Data Science (NumPy, Scikit-Learn)", "importance": "High", "weight": 25},
            {"name": "Supervised & Unsupervised Learning Concepts", "importance": "High", "weight": 20},
            {"name": "Computer Vision Basics (OpenCV)", "importance": "High", "weight": 15},
            {"name": "Model Evaluation Metrics (Precision, Recall, F1, ROC)", "importance": "High", "weight": 15},
            {"name": "Data Preprocessing & Feature Engineering", "importance": "Medium", "weight": 15},
            {"name": "Neural Networks & Deep Learning Foundations", "importance": "Medium", "weight": 10}
        ],
        "recommended_projects": [
            "OpenCV Facial Recognition Attendance System with Anti-Spoofing",
            "Predictive Anomaly Detection on IoT Telemetry with Scikit-Learn",
            "Text Classification or Resume Skill Extraction NLP Pipeline"
        ],
        "interview_topics": [
            "Bias-Variance Tradeoff and Overfitting Prevention",
            "Supervised vs Unsupervised vs Reinforcement Learning",
            "Confusion Matrix, Precision, Recall, and Accuracy paradox",
            "Image Processing Kernels, Edge Detection, and Feature Extraction in OpenCV",
            "Gradient Descent and Loss Functions"
        ]
    },
    "ECE Engineer": {
        "title": "Electronics & Communication Engineer (ECE)",
        "category": "Core & Embedded Systems",
        "description": "Specializes in embedded systems, microcontrollers, IoT sensor telemetry, signal processing, and communication protocols.",
        "core_skills": [
            {"name": "Microcontrollers & Embedded C (ESP32 / Arduino / ARM)", "importance": "High", "weight": 25},
            {"name": "IoT Protocols (MQTT, HTTP, WebSockets, UART, I2C, SPI)", "importance": "High", "weight": 20},
            {"name": "Digital & Analog Electronics Principles", "importance": "High", "weight": 15},
            {"name": "Sensor Interfacing & Signal Acquisition", "importance": "High", "weight": 15},
            {"name": "Digital Twin & Real-Time Monitoring Systems", "importance": "Medium", "weight": 15},
            {"name": "Python for Hardware Telemetry & Automation", "importance": "Medium", "weight": 10}
        ],
        "recommended_projects": [
            "SmartLabTwinAI: Digital Twin with ESP32, Temp/Voltage Monitoring & Anomaly Detection",
            "Industrial Automated Motor Control with IoT Telemetry and MQTT",
            "Real-Time Wireless Sensor Network with Power Management"
        ],
        "interview_topics": [
            "I2C vs SPI vs UART Communication Protocols: Clocking, Speeds, and Bus Topology",
            "Analog-to-Digital Conversion (ADC), Sampling Rate, and Nyquist Theorem",
            "ESP32 Wi-Fi/Bluetooth Architecture and Power Sleep Modes",
            "Digital Twin Architecture: Virtual Models, Sensor Telemetry, and Predictive Maintenance",
            "Feedback Amplifiers, Op-Amp Circuits, and Signal Filtering"
        ]
    },
    "Custom Role": {
        "title": "Technology Professional",
        "category": "General Engineering",
        "description": "Multi-disciplinary technologist with cross-cutting software engineering, problem solving, and analytical capabilities.",
        "core_skills": [
            {"name": "Problem Solving & Algorithmic Thinking", "importance": "High", "weight": 25},
            {"name": "Core Programming (Python / JS / C++)", "importance": "High", "weight": 20},
            {"name": "System Architecture & Design", "importance": "High", "weight": 20},
            {"name": "Database & Storage Management", "importance": "Medium", "weight": 15},
            {"name": "Technical Communication & Collaboration", "importance": "High", "weight": 20}
        ],
        "recommended_projects": [
            "End-to-End Applied Engineering Application",
            "Integrated Hardware-Software Telemetry System",
            "AI-Assisted Workflow Automation Platform"
        ],
        "interview_topics": [
            "Software Development Lifecycle (SDLC) and Agile Methodologies",
            "Modular Code Architecture and Clean Code Practices",
            "Troubleshooting, Debugging, and Root Cause Analysis",
            "Technical Trade-off Decisions and Scalability Planning"
        ]
    }
}

# Rich Question Bank for Mock Interviews
QUESTION_BANK = {
    "Software Developer": {
        "Beginner": {
            "Technical": [
                "Explain the four core principles of Object-Oriented Programming (OOP) with real-world analogies.",
                "What is the difference between an Array and a Linked List? When would you choose one over the other?",
                "How does a Hash Table achieve average O(1) time complexity for search operations, and how are collisions resolved?",
                "Explain the difference between SQL (relational) and NoSQL databases. Give an example scenario for each.",
                "What is a RESTful API? Explain the significance of standard HTTP methods like GET, POST, PUT, and DELETE."
            ],
            "HR": [
                "Tell me about yourself, your educational background in ECE, and why you are interested in software development.",
                "Describe a challenging technical bug or problem you encountered during a project. How did you resolve it?",
                "How do you prioritize your time when balancing university coursework, exams, and personal coding projects?",
                "Where do you see yourself professionally in the next 3 to 5 years?",
                "Why should our company hire you as a software development trainee?"
            ],
            "Mixed": [
                "Introduce yourself and explain what motivated you to build software applications alongside your engineering studies.",
                "Explain the concept of time complexity and Big O notation using a simple sorting algorithm example.",
                "Tell me about a time you had to learn a new technology or framework quickly for a college project.",
                "What is the difference between synchronous and asynchronous execution in modern programming?",
                "How do you handle constructive feedback or code reviews on your work?"
            ]
        },
        "Intermediate": {
            "Technical": [
                "Explain how Python manages memory internally. What is reference counting and how does the Garbage Collector handle cyclic references?",
                "Design a scalable REST API endpoint for user authentication. What security precautions (e.g., password hashing, JWT expiration, CORS) would you implement?",
                "Compare SQL indexing methods. What happens under the hood when a B-Tree index is created on a database table?",
                "Explain how you would design a rate limiter to prevent API abuse in a web application.",
                "What are microservices compared to monolithic architectures? What are the key trade-offs in data consistency and network latency?"
            ],
            "HR": [
                "Describe a situation where you had a disagreement with a project team member regarding architectural choices. How did you handle it?",
                "How do you stay updated with rapidly evolving software frameworks, libraries, and AI technologies?",
                "Tell me about a project where you failed or did not meet your initial timeline. What did you learn from the experience?",
                "What kind of team culture and work environment brings out your best performance?",
                "How do you ensure code maintainability and documentation when working under tight deadlines?"
            ],
            "Mixed": [
                "Explain the Model-View-Controller (MVC) architectural pattern and how Flask or similar web frameworks implement it.",
                "Describe a complex project you built, the architecture decisions you made, and what you would do differently in version 2.",
                "How do you prevent SQL injection and Cross-Site Scripting (XSS) vulnerabilities in web applications?",
                "Tell me about a time you had to mentor or explain a complex technical topic to a peer.",
                "What are database transactions, and how do ACID properties protect data integrity during concurrent writes?"
            ]
        },
        "Advanced": {
            "Technical": [
                "Architect a high-throughput, distributed event-driven notification system that can handle 100,000 requests per minute with guaranteed delivery.",
                "Explain the CAP theorem. How would you choose between CP and AP consistency models for a real-time banking transaction service versus a social media feed?",
                "How would you optimize a slow database query operating on a table with 50 million rows? Detail your diagnostic process.",
                "Discuss memory leaks in long-running Python/Node services and the profiling tools you would use to pinpoint uncollected objects.",
                "How do you implement distributed locking using Redis or ZooKeeper to prevent race conditions across multiple server instances?"
            ],
            "HR": [
                "How do you lead technical decision-making when there is no clear consensus among senior engineers?",
                "Describe how you manage technical debt versus delivering urgent business features.",
                "Tell me about a critical production incident or major bug that occurred on your watch. How did you triage and post-mortem it?",
                "How do you cultivate engineering best practices, such as automated testing and CI/CD, within a growing team?",
                "What is your philosophy on balancing technical perfection with shipping pragmatic solutions?"
            ],
            "Mixed": [
                "Explain how you would architect a real-time IoT digital twin telemetry pipeline handling thousands of streaming sensor events.",
                "Tell me about a time you had to evaluate two competing technologies and justify your final choice to stakeholders.",
                "How do you design database sharding and read-replica strategies to handle rapid horizontal scale?",
                "Describe your approach to code reviews, mentorship, and maintaining high engineering standards.",
                "What strategies do you use for zero-downtime database schema migrations in a high-traffic production system?"
            ]
        }
    },
    "Python Developer": {
        "Beginner": {
            "Technical": [
                "What are the main differences between Python lists, tuples, dictionaries, and sets? Explain with use cases.",
                "How does Python's `is` operator differ from the `==` operator?",
                "Explain what Python list comprehensions and dictionary comprehensions are with syntax examples.",
                "What is the difference between `break`, `continue`, and `pass` in Python loops?",
                "How do you handle exceptions in Python using `try`, `except`, `else`, and `finally` blocks?"
            ],
            "HR": [
                "What sparked your interest in Python programming, and what projects have you built using it?",
                "How do you approach debugging when a Python script throws an unexpected traceback?",
                "Describe a project where you used Python libraries like OpenCV, Flask, or Pandas.",
                "How do you structure your study habits when mastering new libraries?",
                "Why do you want to start your software engineering career as a Python developer?"
            ],
            "Mixed": [
                "Explain the concept of functions as first-class citizens in Python.",
                "Tell me about a practical Python automation script or web app you developed.",
                "What is the purpose of virtual environments (`venv`) in Python development?",
                "How do you collaborate with others using Git when building Python applications?",
                "Explain Python's `*args` and `**kwargs` with an example of where they are useful."
            ]
        },
        "Intermediate": {
            "Technical": [
                "Explain Python decorators: how they work under the hood using closures, and write a simple execution time logging decorator.",
                "What are Python generators and the `yield` keyword? How do they provide memory efficiency over standard lists for large datasets?",
                "Explain the Global Interpreter Lock (GIL) in CPython. How does it affect CPU-bound vs I/O-bound concurrency, and how do you bypass it?",
                "How do you structure a scalable Flask application using Blueprints, Application Factories, and Config objects?",
                "Explain Python's magic/dunder methods (e.g., `__init__`, `__str__`, `__repr__`, `__enter__`, `__exit__`) and how they enable the context manager protocol."
            ],
            "HR": [
                "Describe how you test your Python code. Have you used `unittest` or `pytest`?",
                "Tell me about a time you optimized a slow Python algorithm or database query in your project.",
                "How do you handle situations where third-party packages have conflicting dependencies?",
                "What is your approach to writing clean, readable Python code adhering to PEP 8?",
                "Describe a collaborative project where you integrated Python backend services with frontend interfaces."
            ],
            "Mixed": [
                "Explain how Python's `asyncio` event loop works and how it differs from multi-threading.",
                "Walk me through the architecture of your 'AI Smart Attendance System' and how Flask coordinates face recognition with SQLite.",
                "What are Python metaclasses and when would you use them versus class decorators?",
                "How do you manage database migrations when modifying SQLite or PostgreSQL schemas in Flask?",
                "Tell me about a time you identified and fixed a race condition or file I/O bottleneck in Python."
            ]
        },
        "Advanced": {
            "Technical": [
                "Deep dive into CPython object model: How does Python represent integers, strings, and custom objects in memory? How does string interning and small integer caching work?",
                "Architect a distributed Python worker pool using Celery, Redis, and Asyncio for heavy batch computer vision processing.",
                "Explain the internals of Python descriptor protocol (`__get__`, `__set__`, `__delete__`) and how properties and ORM attributes leverage it.",
                "How would you profile CPU and memory bottlenecks in a production Flask API using cProfile, py-spy, and memory_profiler?",
                "Compare Cython, PyPy, and C-extensions for accelerating compute-heavy numerical and image processing routines."
            ],
            "HR": [
                "How do you advocate for code quality, type hints (mypy), and test coverage in a team resistant to strict linting?",
                "Describe your experience architecting a mission-critical backend service from scratch.",
                "How do you handle production outages in Python microservices under SLA pressure?",
                "What is your philosophy on using micro-frameworks (Flask) versus batteries-included frameworks (Django)?",
                "How do you stay abreast of major Python release features (e.g., Python 3.12+ subinterpreters, free-threaded CPython)?"
            ],
            "Mixed": [
                "How would you design a fault-tolerant Python WebSocket server for streaming real-time IoT digital twin metrics to hundreds of web clients?",
                "Explain how Python's `multiprocessing` module communicates across processes (Pipes, Queues, Shared Memory) and its overhead compared to threads.",
                "Tell me about a complex data pipeline you built and how you ensured idempotency and data integrity.",
                "Describe your strategy for automated containerized deployment using Docker and GitHub Actions.",
                "How do you implement custom serialization/deserialization protocols for high-speed binary data transfer in Python?"
            ]
        }
    },
    "ECE Engineer": {
        "Beginner": {
            "Technical": [
                "Explain the fundamental difference between a Microprocessor (e.g., Intel/ARM CPU) and a Microcontroller (e.g., ESP32/ATmega328P).",
                "What is Pulse Width Modulation (PWM) and how is it used to control motor speeds or LED brightness?",
                "Explain the working principle of the I2C communication protocol. Why are pull-up resistors required on SDA and SCL lines?",
                "What is an Analog-to-Digital Converter (ADC)? Explain the significance of ADC resolution (e.g., 10-bit vs 12-bit).",
                "Explain Ohm's Law and Kirchhoff's Laws (KCL and KVL) with a simple circuit example."
            ],
            "HR": [
                "What inspired you to choose Electronics and Communication Engineering at Mohan Babu University?",
                "Tell me about a hands-on hardware project or lab experiment you enjoyed building most.",
                "How do you bridge the gap between core hardware circuits and software/AI programming?",
                "Describe a time when a hardware circuit didn't work on the breadboard. How did you troubleshoot it?",
                "Where do you see the future of IoT and embedded systems over the next decade?"
            ],
            "Mixed": [
                "Introduce your project 'SmartLabTwinAI' and explain how the ESP32 captures environmental and electrical metrics.",
                "What is the difference between SPI and UART communication protocols in terms of speed, pin count, and duplexity?",
                "How do you handle sensor calibration and noise filtering in embedded IoT systems?",
                "Tell me about a time you collaborated on an engineering project under tight lab deadlines.",
                "Explain how voltage dividers work and why they are needed when interfacing 5V sensors with 3.3V microcontrollers."
            ]
        },
        "Intermediate": {
            "Technical": [
                "Explain the ESP32 power management modes (Active, Modem-sleep, Light-sleep, Deep-sleep) and how to configure GPIO interrupts for wake-up.",
                "How do you implement an AI anomaly detection model on real-time voltage, current, and temperature telemetry from an IoT testbench?",
                "Explain the Nyquist-Shannon sampling theorem and the role of anti-aliasing low-pass filters in analog signal acquisition.",
                "Compare MQTT, HTTP, and WebSockets for real-time IoT device telemetry streaming. Which is optimal for low-bandwidth networks?",
                "Explain the operation of operational amplifiers (Op-Amps) in inverting, non-inverting, and differential instrumentation configurations."
            ],
            "HR": [
                "How do you approach designing an embedded system with strict power consumption constraints?",
                "Describe how you document hardware schematics, pinout maps, and firmware code for team collaboration.",
                "Tell me about a technical setback you faced while integrating hardware sensors with web backends.",
                "How do you prioritize component selection (cost vs reliability vs power) when planning a prototype?",
                "What makes an ECE engineer uniquely equipped to build IoT and AI digital twin systems?"
            ],
            "Mixed": [
                "Walk me through the digital twin architecture of SmartLabTwinAI from physical sensors to web dashboard visualization.",
                "How do you prevent floating inputs and ground loops in mixed analog-digital embedded circuits?",
                "Explain how FreeRTOS tasks and queues can be utilized on ESP32 dual-core processors for concurrent sensing and Wi-Fi transmission.",
                "Tell me about a time you diagnosed a firmware crash using serial logs and oscilloscopes/multimeters.",
                "How do you ensure secure over-the-air (OTA) firmware updates for deployed IoT devices?"
            ]
        },
        "Advanced": {
            "Technical": [
                "Architect a high-reliability industrial IoT digital twin gateway capable of aggregating 50+ sensor nodes over RS485/Modbus and LoRa, publishing to cloud via MQTT/TLS.",
                "Design a hardware-software watchdog and brownout detection strategy for battery-operated remote microcontrollers.",
                "Explain how you would design a Kalman Filter or Moving Average Digital Filter to denoise high-frequency sensor readings on an edge microcontroller.",
                "Discuss PCB layout design rules for high-speed digital and RF traces to minimize electromagnetic interference (EMI) and crosstalk.",
                "How do you implement TinyML / TensorFlow Lite for Microcontrollers to run inference directly on an ESP32 or ARM Cortex-M4 device?"
            ],
            "HR": [
                "How do you manage supply chain risks and component obsolescence in commercial embedded product design?",
                "Describe your experience leading a multi-disciplinary team combining hardware, firmware, and cloud software engineers.",
                "How do you approach safety-critical embedded systems where system failure has physical consequences?",
                "What is your vision for integrating generative AI and digital twins into industrial maintenance?",
                "How do you mentor junior engineers in embedded hardware debugging and schematic analysis?"
            ],
            "Mixed": [
                "Explain how you would scale SmartLabTwinAI across a multi-building university campus with automated energy shedding.",
                "Describe the trade-offs between Edge AI processing on microcontrollers versus Cloud AI inference for anomaly detection.",
                "How do you design hardware ESD protection and surge suppression for industrial laboratory power monitoring?",
                "Tell me about an innovative engineering solution you developed to solve a real-world resource limitation.",
                "Explain the clock synchronization protocols (e.g., NTP, PTP) used across distributed sensor networks."
            ]
        }
    },
    "Web Developer": {
        "Beginner": {
            "Technical": [
                "Explain the CSS Box Model (Content, Padding, Border, Margin) and the difference between `box-sizing: content-box` and `border-box`.",
                "What is the difference between `let`, `const`, and `var` in modern JavaScript?",
                "Explain how CSS Flexbox works. What is the difference between `justify-content` and `align-items`?",
                "What are semantic HTML tags and why are they important for accessibility and SEO?",
                "How does the browser DOM work, and how does JavaScript add, modify, or remove DOM elements?"
            ],
            "HR": [
                "What motivated you to learn web development, and what is your favorite web project you've built?",
                "How do you test your websites across different screen sizes and browsers?",
                "Describe a situation where a layout broke unexpectedly on mobile and how you fixed it.",
                "How do you stay updated with modern CSS techniques like Container Queries and CSS Grid?",
                "Why are you interested in full-stack web development?"
            ],
            "Mixed": [
                "Explain how you implemented dark mode and glassmorphism styling in your web applications.",
                "Tell me about a time you optimized a website's page load speed or responsiveness.",
                "What is the difference between synchronous and asynchronous JavaScript (`fetch`, `async/await`)?",
                "How do you structure CSS for maintainability without relying on heavy frameworks?",
                "Explain the role of `localStorage` and `sessionStorage` in the browser."
            ]
        },
        "Intermediate": {
            "Technical": [
                "Explain the JavaScript Event Loop, Call Stack, Microtask Queue (Promises), and Macrotask Queue (`setTimeout`).",
                "How do CSS Grid and Flexbox differ in mental model and use cases? When is CSS Grid strictly better?",
                "Explain Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF). How do you defend against them?",
                "How do you optimize Core Web Vitals (Largest Contentful Paint, Interaction to Next Paint, Cumulative Layout Shift)?",
                "Explain how WebSockets enable bidirectional full-duplex communication compared to HTTP long polling."
            ],
            "HR": [
                "How do you handle user feedback when a client or tester finds a UI unintuitive?",
                "Describe your approach to building accessible web interfaces (ARIA, keyboard navigation, color contrast).",
                "Tell me about a challenging frontend bug (e.g., z-index stacking context, layout thrashing) you solved.",
                "How do you decide between using vanilla JavaScript/CSS versus adopting a frontend framework?",
                "What is your workflow for responsive mobile-first UI development?"
            ],
            "Mixed": [
                "Walk me through the frontend architecture of CareerAI and how theme state and dynamic charts are rendered.",
                "Explain JavaScript closures and provide a practical example of data privacy using closures.",
                "How do you handle state management across complex interactive web forms without page reloads?",
                "Tell me about a time you built an interactive dashboard with real-time SVG or Canvas graphs.",
                "Explain how HTTP caching headers (`Cache-Control`, `ETag`) improve web performance."
            ]
        },
        "Advanced": {
            "Technical": [
                "Explain browser critical rendering path: DOM construction, CSSOM, Render Tree, Layout, Paint, and Composite. How do you prevent layout thrashing?",
                "Architect a Progressive Web App (PWA) with Service Workers for offline-first caching, background sync, and push notifications.",
                "How do you implement micro-frontends with module federation, and what are the performance trade-offs?",
                "Explain JavaScript memory leaks (detached DOM nodes, forgotten event listeners, circular references) and how to debug them with Chrome DevTools Memory Profiler.",
                "How do you design a high-performance virtualized list rendering 100,000 rows with 60fps scrolling?"
            ],
            "HR": [
                "How do you lead the technical migration of a legacy monolithic frontend to modern standards?",
                "Describe how you enforce web accessibility (WCAG 2.1 AAA) across large engineering teams.",
                "What is your philosophy on modern frontend tooling complexity and build system overhead?",
                "How do you mentor engineers on writing modular, testable UI components?",
                "Tell me about a time you made a major architectural trade-off for performance over developer convenience."
            ],
            "Mixed": [
                "Explain how you would architect a real-time collaborative workspace with WebRTC and operational transformation (OT/CRDT).",
                "Describe your strategy for zero-layout-shift responsive web typography and dynamic viewport units (`dvh`, `cqw`).",
                "How do you build custom accessible UI components (combobox, dialog, tabs) compliant with WAI-ARIA authoring practices?",
                "Tell me about a time you diagnosed and fixed a severe performance bottleneck in clientside JavaScript.",
                "Explain how modern CSS features like `@layer`, `:has()`, and subgrid revolutionize modern stylesheet architecture."
            ]
        }
    },
    "Data Analyst": {
        "Beginner": {
            "Technical": [
                "Explain the difference between `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL OUTER JOIN` in SQL with diagrams/examples.",
                "What is the difference between `WHERE` and `HAVING` clauses in SQL queries?",
                "How do you handle missing or null values in a dataset using Python Pandas (`isna`, `fillna`, `dropna`)?",
                "Explain the concept of Mean, Median, and Mode. In what distribution is the Median preferred over the Mean?",
                "What is the difference between qualitative (categorical) and quantitative (numerical) data?"
            ],
            "HR": [
                "What made you interested in data analytics and data-driven decision making?",
                "Describe a project where you analyzed a dataset and uncovered an interesting pattern.",
                "How do you explain technical analytical findings to a non-technical audience or manager?",
                "Tell me about a time you worked with a messy, incomplete dataset. How did you clean it?",
                "Why is data ethics and privacy important when conducting analysis?"
            ],
            "Mixed": [
                "Explain how you would analyze laboratory sensor data to identify peak energy consumption hours.",
                "What are the most effective chart types for comparing categories versus showing time-series trends?",
                "Tell me about a time you used SQL aggregations (`GROUP BY`, `COUNT`, `SUM`, `AVG`) on relational data.",
                "How do you validate that your data analysis results are accurate before presenting them?",
                "Explain the concept of correlation and why correlation does not imply causation."
            ]
        },
        "Intermediate": {
            "Technical": [
                "Explain SQL Window Functions (`ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LEAD()`, `LAG()`) with practical query examples.",
                "How do you detect and handle outliers in skewed distributions (Z-score vs Interquartile Range IQR method)?",
                "Explain how to perform exploratory data analysis (EDA) using Pandas, NumPy, and visualization libraries.",
                "What is database normalization (1NF, 2NF, 3NF)? When is deliberate denormalization preferred for analytical OLAP workloads?",
                "Explain hypothesis testing, p-values, Type I and Type II errors, and statistical significance."
            ],
            "HR": [
                "Describe a situation where the data contradicted the stakeholders' initial assumptions. How did you present your findings?",
                "How do you prioritize analytical queries when multiple business departments request urgent reports?",
                "Tell me about a time you automated a manual, repetitive data reporting task using Python scripts.",
                "What is your approach to dashboard design: how do you balance detail with visual clarity?",
                "How do you ensure data governance and reproducibility in your analytical pipelines?"
            ],
            "Mixed": [
                "Walk me through how you would design an automated KPI dashboard for student attendance analytics using SQLite and Python.",
                "Explain Common Table Expressions (CTEs) vs subqueries in SQL and their impact on readability and query execution plans.",
                "How do you handle time-zone conversions and resampling on high-frequency IoT time-series telemetry data?",
                "Tell me about a time you identified a data discrepancy or pipeline bug that distorted reports.",
                "Explain how A/B testing is designed and analyzed to measure product feature effectiveness."
            ]
        },
        "Advanced": {
            "Technical": [
                "Architect an end-to-end data warehouse schema (Star Schema vs Snowflake Schema) with Fact and Dimension tables for an enterprise SaaS platform.",
                "Explain query optimization in distributed SQL engines (BigQuery/Snowflake/PostgreSQL): partitioning, clustering, indexing, and cost analysis.",
                "How do you implement statistical anomaly detection and forecasting on streaming IoT power telemetry using ARIMA or Holt-Winters exponential smoothing?",
                "Discuss data lineage, CDC (Change Data Capture), and maintaining Slowly Changing Dimensions (SCD Type 2).",
                "Explain Monte Carlo simulations and multivariate regression modeling for risk analysis."
            ],
            "HR": [
                "How do you build a data-driven culture across cross-functional teams with varying technical maturity?",
                "Describe your experience presenting strategic insights directly to C-level executives or department heads.",
                "How do you manage trade-offs between perfect data accuracy and the speed needed for tactical business decisions?",
                "What is your approach to mentoring junior analysts in SQL proficiency and critical thinking?",
                "How do you prevent bias in data collection, metric definition, and predictive analytics?"
            ],
            "Mixed": [
                "Explain how you would design a data analytics pipeline for predictive equipment maintenance across university engineering laboratories.",
                "Describe your methodology for optimizing high-latency analytical queries consuming excessive memory.",
                "How do you establish automated data quality monitors and alerting thresholds on incoming sensor streams?",
                "Tell me about a time your data analysis influenced a major strategic or engineering decision.",
                "Explain the mathematical principles of Principal Component Analysis (PCA) for dimensionality reduction."
            ]
        }
    },
    "AI/ML Beginner": {
        "Beginner": {
            "Technical": [
                "What is the difference between Supervised Learning, Unsupervised Learning, and Reinforcement Learning?",
                "Explain Overfitting and Underfitting in Machine Learning models. How can you detect and prevent them?",
                "What are the differences between Classification and Regression tasks? Give two examples of each.",
                "Explain how facial detection works in OpenCV using Haar Cascades or deep learning based detectors.",
                "What is a Confusion Matrix, and what do True Positive, True Negative, False Positive, and False Negative represent?"
            ],
            "HR": [
                "What sparked your curiosity in Artificial Intelligence and Machine Learning?",
                "Tell me about your experience developing the 'AI Smart Attendance System' using OpenCV and Python.",
                "How do you approach learning complex mathematical and algorithmic concepts in AI?",
                "Describe a challenge you faced when training or evaluating a machine learning model.",
                "Where do you think AI will have the greatest impact in electronics and communication engineering?"
            ],
            "Mixed": [
                "Explain how face embeddings (128-dimensional vectors) are generated and matched for facial recognition.",
                "What is the role of feature scaling (Standardization vs Min-Max Normalization) before training models?",
                "Tell me about how machine learning can be applied to IoT sensor telemetry for anomaly detection.",
                "How do you split a dataset into Training, Validation, and Test sets, and why is this separation critical?",
                "Explain why accuracy alone can be misleading for imbalanced datasets."
            ]
        },
        "Intermediate": {
            "Technical": [
                "Explain Precision, Recall, F1-Score, and ROC-AUC. When is Recall prioritized over Precision?",
                "How do Decision Trees, Random Forests, and Gradient Boosting (XGBoost/LightGBM) algorithms work and differ?",
                "Explain how Convolutional Neural Networks (CNNs) process images: what do convolutional kernels, activation functions (ReLU), and pooling layers do?",
                "How do you perform real-time anti-spoofing and liveness detection in computer vision facial recognition systems?",
                "Explain the Bias-Variance Tradeoff and how regularization techniques (L1 Lasso, L2 Ridge, Dropout) mitigate variance."
            ],
            "HR": [
                "How do you ensure responsible AI development, mitigating algorithmic bias in facial recognition or resume screening?",
                "Describe a project where you had to curate, clean, and annotate your own custom dataset from scratch.",
                "Tell me about a time your ML model performed well on training data but failed on real-world test cases.",
                "How do you explain the predictions of a black-box machine learning model to non-technical users?",
                "What is your approach to keeping up with fast-paced AI research papers and open-source models?"
            ],
            "Mixed": [
                "Walk me through the pipeline of deploying an OpenCV computer vision model inside a Flask web application.",
                "Explain Gradient Descent optimization: what is the learning rate, and what happens if it is too high or too low?",
                "How do you handle high-dimensional feature spaces and apply dimensionality reduction techniques like PCA?",
                "Tell me about how you would detect anomalies in voltage and temperature sensor data using Isolation Forests or Autoencoders.",
                "Explain transfer learning and fine-tuning with pre-trained vision models (e.g., MobileNet, ResNet)."
            ]
        },
        "Advanced": {
            "Technical": [
                "Deep dive into the Transformer architecture: Explain Self-Attention, Multi-Head Attention, Positional Encodings, and Query/Key/Value matrix transformations.",
                "Architect an end-to-end edge AI pipeline deploying quantized TinyML models (INT8) on ESP32 or microcontrollers with sub-50ms inference latency.",
                "Explain generative models: How do Variational Autoencoders (VAEs), Diffusion Models, and Large Language Models (LLMs) differ in latent representation and training objectives?",
                "How do you mitigate catastrophic forgetting and hallucination in LLM fine-tuning and Retrieval-Augmented Generation (RAG) systems?",
                "Discuss distributed training paradigms: Data Parallelism, Tensor Parallelism, Pipeline Parallelism, and ZeRO memory optimization."
            ],
            "HR": [
                "How do you establish governance, data privacy, and safety rails when integrating LLMs into user-facing career platforms?",
                "Describe your experience architecting a scalable ML inference service with GPU autoscaling and low-latency queuing.",
                "How do you mentor engineering teams transitioning from classical software development to AI/ML engineering?",
                "What is your assessment of the ethical trade-offs between proprietary foundation models and open-source AI?",
                "Tell me about a time you made a critical algorithmic pivot to solve an intractable machine learning challenge."
            ],
            "Mixed": [
                "Explain how you would architect a real-time multimodal AI career coach that analyzes spoken responses, facial sentiment, and resume text simultaneously.",
                "Describe your strategy for model monitoring: detecting concept drift, data drift, and latency degradation in production ML systems.",
                "How do you optimize vector database indexing (HNSW, IVFFlat) for million-scale semantic skill matching?",
                "Tell me about a time you optimized an AI model's inference throughput using ONNX Runtime, TensorRT, or quantization.",
                "Explain the mathematical principles underlying contrastive learning and embedding spaces (e.g., FaceNet, CLIP)."
            ]
        }
    }
}

# Add fallback questions for any unmatched query
QUESTION_BANK["Custom Role"] = QUESTION_BANK["Software Developer"]
