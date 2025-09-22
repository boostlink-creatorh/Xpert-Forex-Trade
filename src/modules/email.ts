import nodemailer from 'nodemailer';

/**
 * Send an email using SMTP.
 * @param {Object} params
 * @param {string} params.to - Recipient email address
 * @param {string} params.subject - Email subject
 * @param {string} params.text - Plain text content
 * @param {string} params.html - HTML content (optional)
 * @returns {Promise<Object>} - Nodemailer response info
 */
export async function sendEmail({ to, subject, text, html }) {
  // Configure SMTP transport
  const transporter = nodemailer.createTransport({
    host: 'smtp.yourhost.com', // e.g., smtp.gmail.com or Hostinger SMTP host
    port: 587,
    secure: false,
    auth: {
      user: 'your@email.com', // Replace with your SMTP username
      pass: 'your_password',  // Replace with your SMTP password
    },
  });

  // Send email
  const info = await transporter.sendMail({
    from: '"XPERT Forex Trade" <your@email.com>',
    to,
    subject,
    text,
    html,
  });

  return info;
}