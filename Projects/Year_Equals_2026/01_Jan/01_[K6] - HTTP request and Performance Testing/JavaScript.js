import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,
  duration: "15s"
};

export default function () {
  // Make a GET request to the target URL
  const res = http.get('https://quickpizza.grafana.com');

  check(res, {
    "Status is 200.": (r) => r.status === 200
  })

  // Sleep for 1 second to simulate real-world usage
  sleep(1);
}