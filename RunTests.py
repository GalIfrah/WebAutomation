# import sys
# import Config
# if __name__ == '__main__':
#     env = sys.argv[1] if len(sys.argv) > 2 else 'dev'
#
#     if env == 'test':
#         app.config = Config.TestConfig
#     elif env == 'prod':
#         app.config = Config.ProdConfig
#
#     else:
#         raise ValueError('Invalid environment name')