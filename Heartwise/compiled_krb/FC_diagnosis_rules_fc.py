# FC_diagnosis_rules_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def shortness(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'shortness_of_breath', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('symptoms', 'shortnessOfBreath',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fatigue(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'fatigue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('symptoms', 'fatigue',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def chestPain(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('symptoms', 'chestPain',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_major_symptoms(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'shortness_of_breath', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'fatigue', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'chest_pain', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def LS_Heart_failure(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('symptoms', 'shortnessOfBreath', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'irregular_heartbeat', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'coughing', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def RS_Heart_failure(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('symptoms', 'shortnessOfBreath', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'irregular_heartbeat', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'leg_swelling', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'abdominal_swelling', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'weight_gain', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        with knowledge_base.Gen_once if index == 5 \
                                 else engine.lookup('symptoms', 'inconclusive', context,
                                                    rule.foreach_patterns(5)) \
                          as gen_5:
                          for dummy in gen_5:
                            engine.assert_('symptoms', 'diagnosis',
                                           (rule.pattern(0).as_data(context),)),
                            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def RS_Heart_failure2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('symptoms', 'shortnessOfBreath', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'irregular_heartbeat', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'abdominal_swelling', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'weight_gain', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('symptoms', 'diagnosis',
                                   (rule.pattern(0).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def RS_Heart_failure3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('symptoms', 'shortnessOfBreath', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'irregular_heartbeat', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'leg_swelling', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'weight_gain', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('symptoms', 'diagnosis',
                                   (rule.pattern(0).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def RS_Heart_failure4(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('symptoms', 'shortnessOfBreath', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'irregular_heartbeat', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'leg_swelling', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'abdominal_swelling', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('symptoms', 'diagnosis',
                                   (rule.pattern(0).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def RS_Heart_failure5(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('symptoms', 'shortnessOfBreath', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'irregular_heartbeat', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'abdominal_swelling', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def RS_Heart_failure6(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('symptoms', 'shortnessOfBreath', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'irregular_heartbeat', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'leg_swelling', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def coronary_artery(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'heart_attack', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'cholesterol', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'Family_history', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'highBloodPressure', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        with knowledge_base.Gen_once if index == 5 \
                                 else engine.lookup('questions', 'smoking', context,
                                                    rule.foreach_patterns(5)) \
                          as gen_5:
                          for dummy in gen_5:
                            engine.assert_('symptoms', 'diagnosis',
                                           (rule.pattern(0).as_data(context),)),
                            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def coronary_artery1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'cholesterol', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'Family_history', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'highBloodPressure', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'smoking', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        engine.assert_('symptoms', 'diagnosis',
                                       (rule.pattern(0).as_data(context),)),
                        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def coronary_artery2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'heart_attack', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'cholesterol', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def coronary_artery3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'cholesterol', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'Family_history', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def coronary_artery4(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'cholesterol', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'smoking', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_attack(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'upper_body', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'cold_sweat', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'indigestion', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('symptoms', 'diagnosis',
                                   (rule.pattern(0).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_attack2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'upper_body', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'cold_sweat', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_attack3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'upper_body', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'indigestion', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_attack4(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'upper_body', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('symptoms', 'diagnosis',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def tachycardia_arrhythmia(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'fluttering', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'racing', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'anxiety', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'faint', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('symptoms', 'diagnosis',
                                   (rule.pattern(0).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def bradycardia_arrhythmia(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'slow', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'dizzy', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'memory', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'faint', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('symptoms', 'diagnosis',
                                   (rule.pattern(0).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_valve_disease_regurgitation(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'heart_murmur', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'abdominal_swelling', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'leg_swelling', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'dizzy', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'faint', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        engine.assert_('symptoms', 'diagnosis',
                                       (rule.pattern(0).as_data(context),)),
                        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_valve_disease1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'heart_murmur', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'dizzy', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'faint', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_valve_disease2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'heart_murmur', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'dizzy', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('symptoms', 'diagnosis',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_valve_disease3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'heart_murmur', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'faint', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('symptoms', 'diagnosis',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_valve_disease4(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'heart_murmur', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('symptoms', 'diagnosis',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('FC_diagnosis_rules')
  
  fc_rule.fc_rule('shortness', This_rule_base, shortness,
    (('questions', 'shortness_of_breath',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fatigue', This_rule_base, fatigue,
    (('questions', 'fatigue',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('chestPain', This_rule_base, chestPain,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_major_symptoms', This_rule_base, no_major_symptoms,
    (('questions', 'shortness_of_breath',
      (pattern.pattern_literal(False),),
      False),
     ('questions', 'fatigue',
      (pattern.pattern_literal(False),),
      False),
     ('questions', 'chest_pain',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal("No heart disease symptoms detected!"),))
  
  fc_rule.fc_rule('LS_Heart_failure', This_rule_base, LS_Heart_failure,
    (('symptoms', 'shortnessOfBreath',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'irregular_heartbeat',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'coughing',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Left sided heart failure"),))
  
  fc_rule.fc_rule('RS_Heart_failure', This_rule_base, RS_Heart_failure,
    (('symptoms', 'shortnessOfBreath',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'irregular_heartbeat',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'leg_swelling',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'abdominal_swelling',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'weight_gain',
      (pattern.pattern_literal(True),),
      False),
     ('symptoms', 'inconclusive',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Right sided heart failure"),))
  
  fc_rule.fc_rule('RS_Heart_failure2', This_rule_base, RS_Heart_failure2,
    (('symptoms', 'shortnessOfBreath',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'irregular_heartbeat',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'abdominal_swelling',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'weight_gain',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Right sided heart failure"),))
  
  fc_rule.fc_rule('RS_Heart_failure3', This_rule_base, RS_Heart_failure3,
    (('symptoms', 'shortnessOfBreath',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'irregular_heartbeat',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'leg_swelling',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'weight_gain',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Right sided heart failure"),))
  
  fc_rule.fc_rule('RS_Heart_failure4', This_rule_base, RS_Heart_failure4,
    (('symptoms', 'shortnessOfBreath',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'irregular_heartbeat',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'leg_swelling',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'abdominal_swelling',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Right sided heart failure"),))
  
  fc_rule.fc_rule('RS_Heart_failure5', This_rule_base, RS_Heart_failure5,
    (('symptoms', 'shortnessOfBreath',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'irregular_heartbeat',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'abdominal_swelling',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Right sided heart failure"),))
  
  fc_rule.fc_rule('RS_Heart_failure6', This_rule_base, RS_Heart_failure6,
    (('symptoms', 'shortnessOfBreath',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'irregular_heartbeat',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'leg_swelling',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Right sided heart failure"),))
  
  fc_rule.fc_rule('coronary_artery', This_rule_base, coronary_artery,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'heart_attack',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cholesterol',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'Family_history',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'highBloodPressure',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'smoking',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Coronary artery disease"),))
  
  fc_rule.fc_rule('coronary_artery1', This_rule_base, coronary_artery1,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cholesterol',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'Family_history',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'highBloodPressure',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'smoking',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Coronary artery disease"),))
  
  fc_rule.fc_rule('coronary_artery2', This_rule_base, coronary_artery2,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'heart_attack',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cholesterol',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Coronary artery disease"),))
  
  fc_rule.fc_rule('coronary_artery3', This_rule_base, coronary_artery3,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cholesterol',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'Family_history',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Coronary artery disease"),))
  
  fc_rule.fc_rule('coronary_artery4', This_rule_base, coronary_artery4,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cholesterol',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'smoking',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Coronary artery disease"),))
  
  fc_rule.fc_rule('heart_attack', This_rule_base, heart_attack,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'upper_body',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cold_sweat',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'indigestion',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Infraction (Heart attack)"),))
  
  fc_rule.fc_rule('heart_attack2', This_rule_base, heart_attack2,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'upper_body',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cold_sweat',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Infraction (Heart attack)"),))
  
  fc_rule.fc_rule('heart_attack3', This_rule_base, heart_attack3,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'upper_body',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'indigestion',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Infraction (Heart attack)"),))
  
  fc_rule.fc_rule('heart_attack4', This_rule_base, heart_attack4,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'upper_body',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Infraction (Heart attack)"),))
  
  fc_rule.fc_rule('tachycardia_arrhythmia', This_rule_base, tachycardia_arrhythmia,
    (('questions', 'fluttering',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'racing',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'anxiety',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'faint',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Tachycardia Arrhythmia"),))
  
  fc_rule.fc_rule('bradycardia_arrhythmia', This_rule_base, bradycardia_arrhythmia,
    (('questions', 'slow',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'dizzy',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'memory',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'faint',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Bradycardia Arrhythmia"),))
  
  fc_rule.fc_rule('heart_valve_disease_regurgitation', This_rule_base, heart_valve_disease_regurgitation,
    (('questions', 'heart_murmur',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'abdominal_swelling',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'leg_swelling',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'dizzy',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'faint',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Valve Disease (valve regurgitation)"),))
  
  fc_rule.fc_rule('heart_valve_disease1', This_rule_base, heart_valve_disease1,
    (('questions', 'heart_murmur',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'dizzy',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'faint',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Valve Disease"),))
  
  fc_rule.fc_rule('heart_valve_disease2', This_rule_base, heart_valve_disease2,
    (('questions', 'heart_murmur',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'dizzy',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Valve Disease"),))
  
  fc_rule.fc_rule('heart_valve_disease3', This_rule_base, heart_valve_disease3,
    (('questions', 'heart_murmur',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'faint',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Valve Disease"),))
  
  fc_rule.fc_rule('heart_valve_disease4', This_rule_base, heart_valve_disease4,
    (('questions', 'heart_murmur',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Valve Disease"),))


Krb_filename = '..\\FC_diagnosis_rules.krb'
Krb_lineno_map = (
    ((12, 16), (6, 6)),
    ((17, 18), (8, 8)),
    ((27, 31), (12, 12)),
    ((32, 33), (14, 14)),
    ((42, 46), (18, 18)),
    ((47, 48), (20, 20)),
    ((57, 61), (25, 25)),
    ((62, 66), (26, 26)),
    ((67, 71), (27, 27)),
    ((72, 73), (29, 29)),
    ((82, 86), (34, 34)),
    ((87, 91), (35, 35)),
    ((92, 96), (36, 36)),
    ((97, 98), (38, 38)),
    ((107, 111), (43, 43)),
    ((112, 116), (44, 44)),
    ((117, 121), (45, 45)),
    ((122, 126), (46, 46)),
    ((127, 131), (47, 47)),
    ((132, 136), (48, 48)),
    ((137, 138), (50, 50)),
    ((147, 151), (58, 58)),
    ((152, 156), (59, 59)),
    ((157, 161), (60, 60)),
    ((162, 166), (61, 61)),
    ((167, 168), (63, 63)),
    ((177, 181), (67, 67)),
    ((182, 186), (68, 68)),
    ((187, 191), (69, 69)),
    ((192, 196), (70, 70)),
    ((197, 198), (72, 72)),
    ((207, 211), (76, 76)),
    ((212, 216), (77, 77)),
    ((217, 221), (78, 78)),
    ((222, 226), (79, 79)),
    ((227, 228), (81, 81)),
    ((237, 241), (85, 85)),
    ((242, 246), (86, 86)),
    ((247, 251), (87, 87)),
    ((252, 253), (89, 89)),
    ((262, 266), (93, 93)),
    ((267, 271), (94, 94)),
    ((272, 276), (95, 95)),
    ((277, 278), (97, 97)),
    ((287, 291), (101, 101)),
    ((292, 296), (102, 102)),
    ((297, 301), (103, 103)),
    ((302, 306), (104, 104)),
    ((307, 311), (105, 105)),
    ((312, 316), (106, 106)),
    ((317, 318), (109, 109)),
    ((327, 331), (114, 114)),
    ((332, 336), (115, 115)),
    ((337, 341), (116, 116)),
    ((342, 346), (117, 117)),
    ((347, 351), (118, 118)),
    ((352, 353), (121, 121)),
    ((362, 366), (126, 126)),
    ((367, 371), (127, 127)),
    ((372, 376), (128, 128)),
    ((377, 378), (130, 130)),
    ((387, 391), (136, 136)),
    ((392, 396), (137, 137)),
    ((397, 401), (138, 138)),
    ((402, 403), (140, 140)),
    ((412, 416), (146, 146)),
    ((417, 421), (147, 147)),
    ((422, 426), (148, 148)),
    ((427, 428), (151, 151)),
    ((437, 441), (157, 157)),
    ((442, 446), (158, 158)),
    ((447, 451), (159, 159)),
    ((452, 456), (160, 160)),
    ((457, 458), (163, 163)),
    ((467, 471), (168, 168)),
    ((472, 476), (169, 169)),
    ((477, 481), (170, 170)),
    ((482, 483), (173, 173)),
    ((492, 496), (178, 178)),
    ((497, 501), (179, 179)),
    ((502, 506), (180, 180)),
    ((507, 508), (183, 183)),
    ((517, 521), (188, 188)),
    ((522, 526), (189, 189)),
    ((527, 528), (192, 192)),
    ((537, 541), (197, 197)),
    ((542, 546), (198, 198)),
    ((547, 551), (199, 199)),
    ((552, 556), (200, 200)),
    ((557, 558), (203, 203)),
    ((567, 571), (208, 208)),
    ((572, 576), (209, 209)),
    ((577, 581), (210, 210)),
    ((582, 586), (211, 211)),
    ((587, 588), (214, 214)),
    ((597, 601), (219, 219)),
    ((602, 606), (220, 220)),
    ((607, 611), (221, 221)),
    ((612, 616), (222, 222)),
    ((617, 621), (223, 223)),
    ((622, 623), (226, 226)),
    ((632, 636), (231, 231)),
    ((637, 641), (232, 232)),
    ((642, 646), (233, 233)),
    ((647, 648), (236, 236)),
    ((657, 661), (241, 241)),
    ((662, 666), (242, 242)),
    ((667, 668), (245, 245)),
    ((677, 681), (249, 249)),
    ((682, 686), (250, 250)),
    ((687, 688), (253, 253)),
    ((697, 701), (258, 258)),
    ((702, 703), (261, 261)),
)
