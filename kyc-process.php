<?php
include 'includes/layout.php';
xpert_header("KYC Verification");
?>

<h2>Verify Your Identity</h2>
<form action="kyc-process.php" method="post" enctype="multipart/form-data" style="max-width:600px;">
  <label for="fullname">Full Name:</label><br>
  <input type="text" id="fullname" name="fullname" required style="width:100%; padding:8px;"><br><br>

  <label for="idfile">Upload ID Document:</label><br>
  <input type="file" id="idfile" name="idfile" required style="width:100%; padding:8px;"><br><br>

  <button type="submit" style="background:#0077cc; color:white; padding:10px 20px; border:none; cursor:pointer;">
    Submit Verification
  </button>
</form>

<p class="audit-note">📍 Hosted at 495 Clermont Ave, Brooklyn, NY · All actions logged for compliance</p>

<?php
xpert_footer();
?>
