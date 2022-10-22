test = {
  'name': 'Submission',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> if "--submit" in sys.argv:
          ...     token = OAuthSession().auth()
          ...     dice = [draw_dice_graphic(num=[i], no_default=True) for i in range(1, 7)]
          ...     submit(dice, DICE_CAPTION, token, lambda x: sys.__stdout__.write(x + "\n"))
          ... else:
          ...     sys.__stdout__.write("Not submitting to gallery, run python ok --submit to do so.\n")
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from design import *
      >>> from hog_gui import *
      >>> from submit import *
      >>> from auth import *
      >>> import sys
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
