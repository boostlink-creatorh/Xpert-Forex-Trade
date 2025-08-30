# 🔥 Firebase Deployment Guide — XPERT Forex Trade

This guide explains how contributors deploy to Firebase Hosting and receive Slack alerts.

## ✅ Prerequisites
- Firebase CLI installed (`npm install -g firebase-tools`)
- `.env` file with:
  - `FIREBASE_TOKEN`
  - `SLACK_WEBHOOK`

## 🚀 Deployment
Push to `main` triggers GitHub Actions:
- Validates `.env`
- Deploys to Firebase Hosting
- Sends Slack alert on success/failure

## 🔐 Secrets
Store tokens securely in GitHub:
- `FIREBASE_TOKEN`: Firebase CI token
- `SLACK_WEBHOOK`: Slack incoming webhook

## 🛡️ Audit Notes
- `.env` is required and validated
- Slack alerts ensure contributor observability
- Workflow is modular and reusable across kits
