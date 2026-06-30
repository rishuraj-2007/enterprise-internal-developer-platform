# Contributing Guide

## Welcome

Thank you for contributing to the Enterprise Internal Developer Platform.

This project follows enterprise software engineering standards. Every contribution should maintain code quality, documentation quality, and production readiness.

---

# Branch Strategy

* main → Production-ready code
* develop → Active development
* feature/* → New features
* bugfix/* → Bug fixes
* hotfix/* → Emergency fixes

---

# Commit Message Convention

Use Conventional Commits.

Examples:

* feat: add user authentication
* fix: resolve API validation issue
* docs: update architecture documentation
* ci: add Azure DevOps pipeline
* test: add backend unit tests
* refactor: improve project structure
* chore: update dependencies

---

# Pull Request Rules

* Keep pull requests focused.
* Write clear descriptions.
* Update documentation when needed.
* Ensure the project builds successfully before merging.
* Request code review before merging into main.

---

# Code Quality Standards

* Follow clean code principles.
* Use meaningful file and variable names.
* Write modular and maintainable code.
* Avoid duplicate code.
* Document public APIs.

---

# Documentation

Every new feature must include:

* Documentation updates
* Architecture updates (if applicable)
* Deployment notes (if applicable)

---

# Security

Never commit:

* Secrets
* API keys
* Passwords
* Certificates
* Environment files containing sensitive data

Use environment variables or secret management solutions.

---

# Testing

Every feature should be tested before merging.

Testing includes:

* Unit Tests
* Integration Tests
* API Testing
* Manual Validation

---

# Goal

Maintain a production-grade, enterprise-quality codebase that reflects real-world DevOps engineering practices.
