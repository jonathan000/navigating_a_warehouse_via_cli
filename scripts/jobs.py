import signal
import sys

import navigate_warehouse_via_cli.schedule as schedule


# pylint: disable=invalid-name
if __name__ == '__main__':
    # Handle the SIGPIPE signal by exiting gracefully when receiving it. This
    # occurs when our output is piped to `head`
    def handle_sigpipe(_, __):
        sys.stdout.close()
        sys.exit(0)
    signal.signal(signal.SIGPIPE, handle_sigpipe)

    # Write table to stdout
    flows = schedule.generate_schedule(seed=2)
    for flow in flows:
        for job in flow.jobs:
            print('\t'.join((
                flow.name,
                str(flow.frequency),
                job.name,
                job.resource_class.value,
                job.output
            )))
