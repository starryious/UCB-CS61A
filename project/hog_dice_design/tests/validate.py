test = {
  'name': 'Output Validation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> for i in range(1, 7):
          ...    assert isinstance(draw_dice_graphic(num=[i], no_default=True), str)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog_gui import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
