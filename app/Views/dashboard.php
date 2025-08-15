<?php include 'header.php'; ?>
<div class="container mt-5">
  <h2 class="mb-4">Welcome, <?= $_SESSION['username']; ?>!</h2>

  <div class="row">
    <div class="col-md-6">
      <h4>Open Trades</h4>
      <ul class="list-group">
        <?php foreach ($openTrades as $trade): ?>
          <li class="list-group-item">
            <?= $trade['pair']; ?> - <?= $trade['direction']; ?> - $<?= $trade['amount']; ?>
          </li>
        <?php endforeach; ?>
      </ul>
    </div>

    <div class="col-md-6">
      <h4>Trade History</h4>
      <ul class="list-group">
        <?php foreach ($tradeHistory as $trade): ?>
          <li class="list-group-item">
            <?= $trade['pair']; ?> - <?= $trade['type']; ?> - <?= $trade['created_at']; ?>
          </li>
        <?php endforeach; ?>
      </ul>
    </div>
  </div>
</div>
<?php include 'footer.php'; ?>
