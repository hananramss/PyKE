# rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def periodontal_disease_gingivitis_rule1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'gums_swollen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.periodontal_disease_gingivitis_rule1: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def periodontal_disease_gingivitis_rule2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'gums_bleeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.periodontal_disease_gingivitis_rule2: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def periodontal_disease_not_gingivitis_rule3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'gums_swollen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.periodontal_disease_not_gingivitis_rule3: got unexpected plan from when clause 1"
            with engine.prove('questions', 'gums_bleeding', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.periodontal_disease_not_gingivitis_rule3: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def periodontal_disease_gingivitis_rule4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'gums_swollen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.periodontal_disease_gingivitis_rule4: got unexpected plan from when clause 1"
            with engine.prove('questions', 'gums_bleeding', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.periodontal_disease_gingivitis_rule4: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def periodontal_disease_periodontitis_rule5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'gums_bleeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.periodontal_disease_periodontitis_rule5: got unexpected plan from when clause 1"
            with engine.prove('questions', 'gums_pull_away_from_the_teeth', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.periodontal_disease_periodontitis_rule5: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def periodontal_disease_not_periodontitis_rule6(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'gums_bleeding', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.periodontal_disease_not_periodontitis_rule6: got unexpected plan from when clause 1"
            with engine.prove('questions', 'gums_pull_away_from_the_teeth', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.periodontal_disease_not_periodontitis_rule6: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dental_abscess_rule1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'gums_swollen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dental_abscess_rule1: got unexpected plan from when clause 1"
            with engine.prove('questions', 'gums_painful', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.dental_abscess_rule1: got unexpected plan from when clause 2"
                with engine.prove('questions', 'intake_medicine', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.dental_abscess_rule1: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'intake_medicine_effective', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.dental_abscess_rule1: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dental_abscess_rule2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'gums_swollen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dental_abscess_rule2: got unexpected plan from when clause 1"
            with engine.prove('questions', 'gums_painful', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.dental_abscess_rule2: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dental_cavity_rule1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'tooth_holes', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dental_cavity_rule1: got unexpected plan from when clause 1"
            with engine.prove('questions', 'tooth_discoloration', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.dental_cavity_rule1: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dental_cavity_rule2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'tooth_holes', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dental_cavity_rule2: got unexpected plan from when clause 1"
            with engine.prove('questions', 'tooth_discoloration', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.dental_cavity_rule2: got unexpected plan from when clause 2"
                with engine.prove('questions', 'tooth_sensitive', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.dental_cavity_rule2: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'toothache', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.dental_cavity_rule2: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'toothache_duration', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.dental_cavity_rule2: got unexpected plan from when clause 5"
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dental_cavity_rule3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'tooth_holes', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dental_cavity_rule3: got unexpected plan from when clause 1"
            with engine.prove('questions', 'tooth_discoloration', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.dental_cavity_rule3: got unexpected plan from when clause 2"
                with engine.prove('questions', 'tooth_sensitive', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.dental_cavity_rule3: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'toothache', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.dental_cavity_rule3: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'toothache_duration', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.dental_cavity_rule3: got unexpected plan from when clause 5"
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dental_cavity_rule4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'tooth_holes', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dental_cavity_rule4: got unexpected plan from when clause 1"
            with engine.prove('questions', 'tooth_discoloration', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.dental_cavity_rule4: got unexpected plan from when clause 2"
                with engine.prove('questions', 'tooth_sensitive', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.dental_cavity_rule4: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'toothache', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.dental_cavity_rule4: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'toothache_duration', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.dental_cavity_rule4: got unexpected plan from when clause 5"
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dental_cavity_rule5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'tooth_holes', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dental_cavity_rule5: got unexpected plan from when clause 1"
            with engine.prove('questions', 'tooth_discoloration', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.dental_cavity_rule5: got unexpected plan from when clause 2"
                with engine.prove('questions', 'tooth_sensitive', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.dental_cavity_rule5: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'toothache', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.dental_cavity_rule5: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'toothache_duration', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.dental_cavity_rule5: got unexpected plan from when clause 5"
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dental_cavity_rule6(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'tooth_holes', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dental_cavity_rule6: got unexpected plan from when clause 1"
            with engine.prove('questions', 'tooth_discoloration', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.dental_cavity_rule6: got unexpected plan from when clause 2"
                with engine.prove('questions', 'tooth_sensitive', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.dental_cavity_rule6: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'toothache', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.dental_cavity_rule6: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'toothache_duration', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.dental_cavity_rule6: got unexpected plan from when clause 5"
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def discolorations_rule1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'smoke_tobacco', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.discolorations_rule1: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def discolorations_rule2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'drink_black_tea', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.discolorations_rule2: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def discolorations_rule3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'use_mouthwash', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.discolorations_rule3: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def discolorations_rule4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'smoke_tobacco', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.discolorations_rule4: got unexpected plan from when clause 1"
            with engine.prove('questions', 'drink_black_tea', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.discolorations_rule4: got unexpected plan from when clause 2"
                with engine.prove('questions', 'use_mouthwash', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.discolorations_rule4: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def discolorations_rule5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'smoke_tobacco', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.discolorations_rule5: got unexpected plan from when clause 1"
            with engine.prove('questions', 'drink_black_tea', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.discolorations_rule5: got unexpected plan from when clause 2"
                with engine.prove('questions', 'use_mouthwash', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.discolorations_rule5: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def discolorations_rule6(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'smoke_tobacco', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.discolorations_rule6: got unexpected plan from when clause 1"
            with engine.prove('questions', 'drink_black_tea', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.discolorations_rule6: got unexpected plan from when clause 2"
                with engine.prove('questions', 'use_mouthwash', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.discolorations_rule6: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  bc_rule.bc_rule('periodontal_disease_gingivitis_rule1', This_rule_base, 'periodontal',
                  periodontal_disease_gingivitis_rule1, None,
                  (pattern.pattern_literal('Gingivitis'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('periodontal_disease_gingivitis_rule2', This_rule_base, 'periodontal',
                  periodontal_disease_gingivitis_rule2, None,
                  (pattern.pattern_literal('Gingivitis'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('periodontal_disease_not_gingivitis_rule3', This_rule_base, 'periodontal',
                  periodontal_disease_not_gingivitis_rule3, None,
                  (pattern.pattern_literal('not_Gingivitis'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('periodontal_disease_gingivitis_rule4', This_rule_base, 'periodontal',
                  periodontal_disease_gingivitis_rule4, None,
                  (pattern.pattern_literal('Gingivitis'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('periodontal_disease_periodontitis_rule5', This_rule_base, 'periodontal',
                  periodontal_disease_periodontitis_rule5, None,
                  (pattern.pattern_literal('periodontitis'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('periodontal_disease_not_periodontitis_rule6', This_rule_base, 'periodontal',
                  periodontal_disease_not_periodontitis_rule6, None,
                  (pattern.pattern_literal('not_periodontitis'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('dental_abscess_rule1', This_rule_base, 'dental_abscess',
                  dental_abscess_rule1, None,
                  (pattern.pattern_literal("\nYou have a high possibility of having a dental abscess."),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('dental_abscess_rule2', This_rule_base, 'dental_abscess',
                  dental_abscess_rule2, None,
                  (pattern.pattern_literal("\nYou don't have a dental abscess."),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('dental_cavity_rule1', This_rule_base, 'dental_cavity',
                  dental_cavity_rule1, None,
                  (pattern.pattern_literal("\nThis indicates an early-stage tooth decay or a cavity. Tooth decay can begin as a small, white spot on the tooth surface, which may not be immediately noticeable. As the decay progresses, it can eventually form a hole or pit in the tooth."),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('dental_cavity_rule2', This_rule_base, 'dental_cavity',
                  dental_cavity_rule2, None,
                  (pattern.pattern_literal("\nThis indicates that dental decay has progressed to a moderate stage. The decay is progressing and requires prompt attention from a dentist. It's essential to seek professional dental care to assess the extent of the decay and determine the appropriate treatment to prevent further damage to the tooth. Regular dental check-ups are crucial for detecting and addressing dental issues in their early stages."),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('dental_cavity_rule3', This_rule_base, 'dental_cavity',
                  dental_cavity_rule3, None,
                  (pattern.pattern_literal("\nThis indicates the presence of early-stage dental decay or enamel erosion. It's essential to address sensitivity and seek professional dental care to prevent further damage to the tooth enamel and underlying structures. Regular dental check-ups are crucial for detecting and addressing dental issues in their early stages."),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('dental_cavity_rule4', This_rule_base, 'dental_cavity',
                  dental_cavity_rule4, None,
                  (pattern.pattern_literal("\nThis indicates advanced dental decay or cavity formation. It's essential to seek prompt professional dental care to assess the extent of the decay and determine the appropriate treatment to prevent further damage to the tooth. Delaying treatment can lead to worsening pain, infection, and potentially the loss of the affected tooth. Regular dental check-ups are crucial for detecting and addressing dental issues in their early stages."),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('dental_cavity_rule5', This_rule_base, 'dental_cavity',
                  dental_cavity_rule5, None,
                  (pattern.pattern_literal("\nThis indicates an advanced dental decay or cavity formation. It's essential to seek prompt professional dental care to assess the extent of the decay and determine the appropriate treatment to prevent further damage to the tooth. Delaying treatment can lead to worsening pain, infection, and potentially the loss of the affected tooth. Regular dental check-ups are crucial for detecting and addressing dental issues in their early stages."),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('dental_cavity_rule6', This_rule_base, 'dental_cavity',
                  dental_cavity_rule6, None,
                  (pattern.pattern_literal("\nNo Dental Cavity Detected"),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('discolorations_rule1', This_rule_base, 'discoloration',
                  discolorations_rule1, None,
                  (pattern.pattern_literal("\nSmoke and chewing tobacco can possibly be the reason of your discoloration teeth"),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('discolorations_rule2', This_rule_base, 'discoloration',
                  discolorations_rule2, None,
                  (pattern.pattern_literal("\nDrinking black drinks can possibly be the reason of your discoloration teeth"),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('discolorations_rule3', This_rule_base, 'discoloration',
                  discolorations_rule3, None,
                  (pattern.pattern_literal("\nUsing mouthwash with chlorhexidine and cetylpyridinium chloride can possibly be the reason of your discoloration teeth"),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('discolorations_rule4', This_rule_base, 'discoloration',
                  discolorations_rule4, None,
                  (pattern.pattern_literal("\nIf the user smokes and chews tobacco but does not consume other staining substances or use specific mouthwashes, their tooth discoloration is most likely due to tobacco use. Regular brushing, flossing, and dental check-ups are essential to mitigate some discoloration. However, quitting smoking and tobacco use is the most effective way to prevent further staining and improve oral health."),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('discolorations_rule5', This_rule_base, 'discoloration',
                  discolorations_rule5, None,
                  (pattern.pattern_literal("\nPreventive Measures: \n\n Rinse After Drinking: Rinse your mouth with water after consuming staining beverages to reduce pigment contact. \n Use a Straw: Drinking through a straw minimizes contact between beverages and your teeth. \n Brush and Floss Regularly: Brush twice a day and floss daily for good oral hygiene. \n Regular Dental Cleanings: Visit your dentist regularly for professional cleanings to remove surface stains and prevent discoloration. \n\n By following these measures, you can reduce the staining effects of beverages on your teeth."),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('discolorations_rule6', This_rule_base, 'discoloration',
                  discolorations_rule6, None,
                  (pattern.pattern_literal("\nNo Discoloration of Teeth Detected"),),
                  (),
                  (pattern.pattern_literal(False),))


Krb_filename = '..\\rules.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 25), (6, 6)),
    ((38, 42), (9, 9)),
    ((44, 49), (11, 11)),
    ((62, 66), (14, 14)),
    ((68, 73), (16, 16)),
    ((74, 79), (17, 17)),
    ((92, 96), (20, 20)),
    ((98, 103), (22, 22)),
    ((104, 109), (23, 23)),
    ((122, 126), (26, 26)),
    ((128, 133), (28, 28)),
    ((134, 139), (29, 29)),
    ((152, 156), (32, 32)),
    ((158, 163), (34, 34)),
    ((164, 169), (35, 35)),
    ((182, 186), (42, 42)),
    ((188, 193), (44, 44)),
    ((194, 199), (45, 45)),
    ((200, 205), (46, 46)),
    ((206, 211), (47, 47)),
    ((224, 228), (50, 50)),
    ((230, 235), (52, 52)),
    ((236, 241), (53, 53)),
    ((254, 258), (60, 60)),
    ((260, 265), (62, 62)),
    ((266, 271), (63, 63)),
    ((284, 288), (66, 66)),
    ((290, 295), (68, 68)),
    ((296, 301), (69, 69)),
    ((302, 307), (70, 70)),
    ((308, 313), (71, 71)),
    ((314, 319), (72, 72)),
    ((332, 336), (75, 75)),
    ((338, 343), (77, 77)),
    ((344, 349), (78, 78)),
    ((350, 355), (79, 79)),
    ((356, 361), (80, 80)),
    ((362, 367), (81, 81)),
    ((380, 384), (84, 84)),
    ((386, 391), (86, 86)),
    ((392, 397), (87, 87)),
    ((398, 403), (88, 88)),
    ((404, 409), (89, 89)),
    ((410, 415), (90, 90)),
    ((428, 432), (93, 93)),
    ((434, 439), (95, 95)),
    ((440, 445), (96, 96)),
    ((446, 451), (97, 97)),
    ((452, 457), (98, 98)),
    ((458, 463), (99, 99)),
    ((476, 480), (102, 102)),
    ((482, 487), (104, 104)),
    ((488, 493), (105, 105)),
    ((494, 499), (106, 106)),
    ((500, 505), (107, 107)),
    ((506, 511), (108, 108)),
    ((524, 528), (114, 114)),
    ((530, 535), (116, 116)),
    ((548, 552), (119, 119)),
    ((554, 559), (121, 121)),
    ((572, 576), (124, 124)),
    ((578, 583), (126, 126)),
    ((596, 600), (129, 129)),
    ((602, 607), (131, 131)),
    ((608, 613), (132, 132)),
    ((614, 619), (133, 133)),
    ((632, 636), (136, 136)),
    ((638, 643), (138, 138)),
    ((644, 649), (139, 139)),
    ((650, 655), (140, 140)),
    ((668, 672), (143, 143)),
    ((674, 679), (145, 145)),
    ((680, 685), (146, 146)),
    ((686, 691), (147, 147)),
)
