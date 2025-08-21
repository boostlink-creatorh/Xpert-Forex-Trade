# 🔐 Security Policy

## 📌 Domain Protection

This repository is maintained by **XpertForexTrade Inc.** and is the only official GitHub source for the trading platform hosted at [xpertforextrad.com](https://xpertforextrad.com). Any other domains, social handles, or repositories claiming affiliation should be treated with caution. If you suspect a clone or impersonation, please report it to [support@xpertforextrad.com](mailto:support@xpertforextrad.com).

## 🚨 Reporting Vulnerabilities

If you discover a security vulnerability in this repo, please report it responsibly via [security@xpertforextrad.com](mailto:security@xpertforextrad.com). Do not open public issues for sensitive disclosures.

## 🔒 Best Practices

- Never commit `.env` files or credentials. `.env` is already listed in `.gitignore`.
- Always validate user input before processing trades or login attempts.
- Use HTTPS for all production deployments.
- Rotate database and API keys regularly.
- Monitor for suspicious activity in the `users` and `trades` tables.

## 🧪 CI/CD & Deployment Notes

This repo includes modular workflows for deployment via GitHub Actions. Contributors should validate all secrets and environment variables before pushing to production. Refer to `ONBOARDING.md` for setup and deployment steps.

## ⚠️ Disclaimer

This software is provided “as is” without warranty of any kind. Use at your own risk. XpertForexTrade Inc. is not liable for financial losses, misconfigurations, or unauthorized deployments.

---

Stay secure. Stay transparent. Build with confidence.
