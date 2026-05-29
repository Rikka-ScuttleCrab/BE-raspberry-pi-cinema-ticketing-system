import time
import threading

from background.ticket_cleanup import (
    cleanup_expired_tickets
)


def start_cleanup_scheduler():

    def run():

        while True:

            cleanup_expired_tickets()

            time.sleep(300)

    thread = threading.Thread(
        target=run,
        daemon=True
    )

    thread.start()