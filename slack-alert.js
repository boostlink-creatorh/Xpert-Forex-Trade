// slack-alert.js
const fs = require('fs');
const axios = require('axios');
require('dotenv').config();

const logPath = './onboarding/logs/fallback-log.txt';
const webhookUrl = process.env.SLACK_WEBHOOK_URL;

function sendSlackAlert(message) {
  return axios.post(webhookUrl, { text: message });
}

function checkLogAndAlert() {
  if (!fs.existsSync(logPath)) return;

  const logContent = fs.readFileSync(logPath, 'utf8');
  const lastEntry = logContent.trim().split('\n').pop();

  if (lastEntry.includes('No runtime logs detected')) {
    sendSlackAlert(`⚠️ Fallback triggered: ${lastEntry}`)
      .then(() => console.log('Slack alert sent.'))
      .catch(err => console.error('Slack alert failed:', err));
  }
}

checkLogAndAlert();
