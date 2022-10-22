test = {
  'name': 'Implicit Biases',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(BIASES.split(' ')) >= 80 # you must write at least 80 words!
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from biases import BIASES
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
