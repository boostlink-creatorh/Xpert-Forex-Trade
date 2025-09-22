import nodemailer from 'nodemailer';

/**
 * Send an email using Hostinger SMTP.
 * @param {Object} params
 * @param {string} params.to - Recipient email address
 * @param {string} params.subject - Email subject
 * @param {string} params.text - Plain text content
 * @param {string} params.html - HTML content (optional)
 * @returns {Promise<Object>} - Nodemailer response info
 */
export async function sendEmail({ to, subject, text, html }) {
  // Hostinger SMTP settings (sending, not POP for receiving)
  const transporter = nodemailer.createTransport({
    host: 'smtp.hostinger.com', // Hostinger SMTP outgoing server
    port: 465,                  // SSL port for SMTP
    secure: true,               // true for port 465 (SSL)
    auth: {
      user: 'info@xpertforextrad.com',    // Hostinger email address
      pass: 'Kapacity$55',                // Hostinger email password
    },
  });

  // Send email
  const info = await transporter.sendMail({
    from: '"XPERT Forex Trade" <info@xpertforextrad.com>',
    to,
    subject,
    text,
    html,
  });

  return info;
}