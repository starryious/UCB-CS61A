test = {
  'name': 'Output Validation',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> for word in ["henlo", "goodbue"]:
          ...    corrected_word = autocorrect(word)
          ...    assert isinstance(corrected_word, str), \
          ...       "Invalid output: autocorrect({}) returned {}".format(word, corrected_word)
          >>> assert \
          ...   isinstance(PLAYER_NAME, str) and 1 <= len(PLAYER_NAME) <= 64, \
          ...   "Invalid team name: {}".format(PLAYER_NAME)
          >>> assert \
          ...   os.path.getsize("./autocorrect.py") <= 3000, \
          ...   "Your file size is too large!"
          >>> score = get_score(TEST_FILE, limit=50)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from autocorrect import autocorrect, PLAYER_NAME
      >>> from score import get_score, TEST_FILE
      >>> import os
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
