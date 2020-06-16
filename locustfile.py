"""Locust file loading scenario."""
from locust import HttpUser, task, between

from service import id_randomizer, status_randomizer


class QuickstartUser(HttpUser):
    """Locust class for user behaviour."""

    wait_time = between(5, 9)

    @task
    def index_page(self) -> None:
        """Getting main page scenario."""
        self.client.get("/")

    @task(1)
    def comment(self) -> None:
        """Posting json  scenario."""
        data = {
            "id": id_randomizer(),
            "status": status_randomizer()
        }
        self.client.post("/post", json=data)

    def on_start(self) -> None:
        """Simple start function."""
        pass
