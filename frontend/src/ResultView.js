function ResultView({ result }) {
  return (
    <div style={{ marginTop: 20 }}>
      <h3>Routing Decision</h3>
      <p><b>Route:</b> {result.recommendedRoute}</p>
      <p><b>Reason:</b> {result.reasoning}</p>
      <pre>{JSON.stringify(result, null, 2)}</pre>
    </div>
  );
}
export default ResultView;
