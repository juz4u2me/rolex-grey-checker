from brightime import Brightime

# print('37mm yacht master')
# bt = Brightime('https://www.championtime.com/brand-category/men/rolex-sport-models-brand-new/', '268622')
# bt.display()
#
# print('\n41mm yacht master')
# bt = Brightime('https://www.championtime.com/brand-category/men/rolex-sport-models-brand-new/', '126622')
# bt.display()
#
# print('\n41mm submariner w/ date')
# bt = Brightime('https://www.championtime.com/brand-category/men/rolex-sport-models-brand-new/', '126610LN')
# bt.display()
#
# print('\n41mm datejust')
# bt = Brightime('https://www.championtime.com/brand-category/men/rolex-classic-brand-new/', '126334')
# bt.display()

bt = Brightime('https://www.championtime.com/brand-category/men/rolex-sport-models-brand-new/', ['268622', '126622', '126610LN'])
bt.display()
