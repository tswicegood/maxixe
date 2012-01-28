from clint.textui import indent, puts


# TODO: move this to the correct home
class TextReporter(object):
    def __init__(self):
        self.current_indent = 2

    def indent(self):
        self.current_indent += 2

    def dedent(self):
        self.current_indent -= 2

    def start_feature(self, feature):
        with indent(self.current_indent):
            puts("Feature: %s" % feature.name)
        with indent(self.current_indent + 2):
            puts(feature.description)
        print ""
        self.indent()

    def stop_feature(self, feature):
        self.dedent()

    def start_scenario(self, scenario):
        with indent(self.current_indent):
            puts("Scenario: %s" % scenario.name)
        self.indent()

    def stop_scenario(self, scenario):
        print ""
        self.dedent()

    def start_step(self, step):
        pass

    def stop_step(self, step):
        with indent(self.current_indent):
            if step.successful:
                suffix = "OK!"
            elif step.skipped:
                suffix = "SKIPPED"
            elif step.failed:
                suffix = "FAILED"
            else:
                suffix = "UNKNOWN"
            puts("%s [%s]" % (step.description, suffix))


class Runner(object):
    def __init__(self, reporter):
        self.reporter = reporter

    def run(self, feature):
        self.reporter.start_feature(feature)
        for scenario in feature.scenarios:
            self.run_scenario(scenario)
        self.reporter.stop_feature(feature)

    def run_scenario(self, scenario):
        self.reporter.start_scenario(scenario)
        continue_running = True
        for step in scenario.steps:
            self.reporter.start_step(step)
            step.run()
            self.reporter.stop_step(step)
        self.reporter.stop_scenario(scenario)
