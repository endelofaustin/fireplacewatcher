#!/usr/bin/env python3

import aws_cdk as cdk

from fireplacewatcher.fireplacewatcher_stack import FireplacewatcherStack


app = cdk.App()
FireplacewatcherStack(app, "FireplacewatcherStack")

app.synth()
