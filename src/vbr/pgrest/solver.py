import logging
import random

__all__ = ["DependencySolver"]


class DependencySolver(object):
    def __init__(self, definitions):

        # Lists of table definitions
        self.to_do = definitions
        self.deferred = []
        # List of table names
        self.completed = []
        # Unresolved dependencies
        self.dependencies = []

    def ordered_emit(self):

        ordered = []
        max_iterations = len(self.to_do) * 4
        iterations = 0

        while self.to_do and (iterations <= max_iterations):

            # find dependencies
            tdef = self.to_do.pop()
            tdef_table_name = tdef["table_name"]
            tdef_cols = tdef["columns"]

            # Are any foreign keys defined? If so, do they
            # refer to tables that have not been completed. If
            # so, put the definition back on the queue
            # print('attempt: ' + tdef_table_name)
            dep_found = False
            deps = []
            for k, v in tdef_cols.items():
                if v.get("foreign_key", False):
                    if v["reference_table"] not in self.completed:
                        # print('dependency: {0} <- {1}'.format(tdef_table_name, v['reference_table']))
                        dep_found = True
                        deps.append(v["reference_table"])
                        # break

            if not dep_found:
                self.completed.append(tdef_table_name)
                # print('completed: ' + ', '.join(self.completed))
                ordered.append(tdef)
            else:
                self.to_do.insert(0, tdef)
                # print('deps: ' + ','.join(deps))

            iterations = iterations + 1
            # print('iteration: ' + str(iterations))
            # random.shuffle(self.to_do)

        if len(self.to_do) > 0:
            fails = ",".join([t["table_name"] for t in self.to_do])
            raise ValueError(
                "Some tables could not be ordered due to unresolved dependencies: {0}".format(
                    fails
                )
            )

        return ordered
