# John Doe Career AI

**A conversational, AI-powered résumé built with Python, Google Gemini, and Career AI Core.**

John Doe Career AI is a fictional, fully customizable example application that demonstrates how to build an interactive professional résumé using [Career AI Core](https://github.com/cmartinferrer/career-ai-core).

Instead of navigating a traditional résumé, visitors can ask natural-language questions about a candidate's professional background, technical skills, work experience, and projects.

This repository is designed as both a **working reference implementation** and a **hands-on learning resource** for developers interested in AI-powered applications.

> **Disclaimer:** John Doe is a fictional candidate. All professional information, companies, projects, and achievements included in this repository are invented for educational purposes.

## What You'll Build

A conversational assistant that can answer questions such as:

- What is John Doe's professional background?
- Which companies has he worked for?
- What experience does he have with Apache Kafka?
- Which technologies did he use at Northstar Digital Solutions?
- What were his responsibilities on the Data Processing Platform?
- What technical challenges did he face in that project?

The assistant uses structured career data and detailed project documentation to generate contextual answers.

## Key Features

- **Conversational résumé:** Explore professional experience through natural-language questions.
- **Context-aware responses:** Ask follow-up questions without repeating the entire context.
- **Structured knowledge base:** Maintain career information using YAML.
- **Detailed project documentation:** Describe technical challenges, responsibilities, and achievements using Markdown.
- **Google Gemini integration:** Generate responses using a configurable Gemini model.
- **Gradio web interface:** Interact with the assistant through a browser.
- **Configurable localization:** Choose between English and Spanish.
- **Request limits:** Configure per-visitor and global request limits.
- **Reusable architecture:** Keep candidate-specific content separate from the underlying framework.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application runtime |
| Career AI Core | Conversational résumé framework |
| Google Gemini | AI language model |
| Gradio | Web-based chat interface |
| YAML | Structured career information |
| Markdown | Detailed project documentation |
| uv | Python dependency and environment management |

## Project Structure

```text
john-career-ai/
├── data/
│   ├── projects/
│   │   └── data-platform.md
│   ├── education.yaml
│   ├── experience.yaml
│   ├── profile.yaml
│   └── skills.yaml
├── .env.example
├── .gitignore
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

The application is intentionally small. Career AI Core handles the reusable application logic, while this repository provides the candidate's knowledge base, configuration, and entry point.

## Getting Started

### 1. Prerequisites

Before starting, make sure you have:

- Python compatible with the installed Career AI Core version.
- [uv](https://docs.astral.sh/uv/) installed.
- A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/).
- Git, if you want to clone the repository.

### 2. Clone the Repository

```bash
git clone https://github.com/cmartinferrer/john-career-ai.git
cd john-career-ai
```

### 3. Install Dependencies

The project uses `uv` to manage its Python environment and dependencies.

```bash
uv sync
```

The dependency on Career AI Core is declared in `pyproject.toml` and resolved through `uv.lock`.

To add Career AI Core manually to a new project:

```bash
uv add "career-ai-core @ git+https://github.com/cmartinferrer/career-ai-core@v0.1.0"
```

Using a specific release tag helps make the installation reproducible.

### 4. Configure Environment Variables

Create a local environment file from the provided template:

```bash
cp .env.example .env
```

Open `.env` and configure your Gemini API key and preferred model.

```dotenv
GOOGLE_API_KEY=your-actual-api-key

CAREER_AI_LOCALE=en
GEMINI_MODEL=your-available-gemini-model

MAX_REQUESTS=20
RATE_LIMIT_WINDOW_SECONDS=3600
GLOBAL_DAILY_REQUEST_LIMIT=200
```

**Configuration reference**

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | API key used to access Google Gemini |
| `CAREER_AI_LOCALE` | Interface language (`en` or `es`) |
| `GEMINI_MODEL` | Gemini model identifier |
| `MAX_REQUESTS` | Maximum requests per visitor within the configured window |
| `RATE_LIMIT_WINDOW_SECONDS` | Rate-limit window duration, in seconds |
| `GLOBAL_DAILY_REQUEST_LIMIT` | Maximum total requests per day |

Use a Gemini model that is currently available to your account and supported by the framework.

**Security:** Never commit your actual `.env` file or expose your API key in a public repository. Only `.env.example` should be version-controlled.

### 5. Run the Application

Start the application from the project root:

```bash
uv run main.py
```

Once Gradio starts, open the local URL displayed in your terminal, typically:

```text
http://127.0.0.1:7860
```

You can now interact with John Doe's conversational résumé.

## Understanding the Knowledge Base

Career AI Core separates professional information from the application code.

This allows you to update the candidate's experience or add new projects without rewriting the conversational interface.

### `data/profile.yaml`

Contains the candidate's professional identity and summary.

Typical information includes the candidate's name, professional title, and career overview.

### `data/experience.yaml`

Describes professional experience, including employers, positions, employment periods, responsibilities, and associated projects.

Experiences can reference skills defined in the shared skills catalog.

### `data/skills.yaml`

Defines technical skills and organizes them into categories.

Each skill has an identifier that can be referenced from experiences and projects.

This makes it possible to maintain consistent skill information across the knowledge base.

### `data/projects/`

Contains Markdown documents describing individual projects in greater detail.

For example, `data-platform.md` documents a fictional event-driven data processing platform.

It includes:

- Business context and objectives.
- Architecture and technologies.
- Responsibilities and contributions.
- Technical challenges and solutions.
- Results and lessons learned.

These documents provide additional context for technical questions.

### `data/education.yaml`

Contains example educational background, courses, and certifications.

**Version note:** Career AI Core `v0.1.0` does not automatically load this file through its standard knowledge loader. It is included as an example of how the knowledge base can be extended, rather than as a currently supported source for chat responses.

## How It Works

The application follows a straightforward flow:

```text
User
  |
  v
Gradio Chat Interface
  |
  v
Career AI Core
  |
  +---- YAML Career Data
  |
  +---- Markdown Project Documentation
  |
  v
Google Gemini
  |
  v
Contextual Response
```

When a user asks a question, Career AI Core combines the conversation context with the candidate's knowledge base and uses Gemini to generate a relevant answer.

The entry point, `main.py`, delegates application startup to the framework.

This separation makes the consumer application easier to understand and maintain.

## Customizing the Application

You can turn this fictional résumé into a different candidate's assistant by updating the knowledge base.

A practical customization workflow is:

1. Update the professional profile in `profile.yaml`.
2. Define technical skills in `skills.yaml`.
3. Add employment history and projects in `experience.yaml`.
4. Create detailed Markdown documents for important projects.
5. Keep skill identifiers and project references consistent.
6. Configure the language, Gemini model, and request limits.
7. Restart the application and test representative questions.

When extending the data, follow the schema supported by your installed Career AI Core version.

Avoid introducing arbitrary YAML fields without checking the framework's data models and validation rules.

## Testing the Assistant

After starting the application, try a short conversation:

**User:** Which companies has John Doe worked for?

**User:** What did he do at Northstar Digital Solutions?

**User:** Which technologies did he use there?

**User:** What were the main technical challenges?

These questions test both factual retrieval and conversational context.

Also verify that the assistant does not invent experience, qualifications, or project achievements that are absent from the knowledge base.

## Security and Deployment Considerations

This example is suitable for local development, experimentation, and learning.

Before deploying it publicly, consider the following:

- Keep API credentials in environment variables or a secure secrets manager.
- Never expose `.env` or other sensitive files.
- Configure appropriate request limits to control API usage.
- Monitor Gemini usage and associated costs.
- Review the knowledge base before publishing personal or confidential information.
- Use appropriate hosting and access controls for your deployment.

**Important:** The built-in request counters are stored in process memory. They are not shared across multiple application instances and reset when the process restarts. Distributed deployments require a shared rate-limiting mechanism for consistent enforcement.

## Career AI Core

This project is powered by **Career AI Core**, a reusable Python framework for building conversational career assistants.

The framework separates the reusable AI application components from candidate-specific data, making it possible to create different conversational résumés using the same underlying architecture.

Explore the framework, its source code, and available releases:

[Career AI Core on GitHub](https://github.com/cmartinferrer/career-ai-core)

This example uses the `v0.1.0` release.

## Contributing

Contributions that improve the example's documentation, developer experience, or educational value are welcome.

If you discover an issue related to the underlying framework rather than this example application, consider reporting it in the Career AI Core repository.

## License

Refer to the repository's `LICENSE` file for the applicable license terms. If no license has been added yet, the project should not be assumed to grant permission for reuse or redistribution.

---

**Built for learning, experimentation, and exploring a more interactive way to present professional experience.**
