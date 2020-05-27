class Config:
    pass

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


main_configs = {'default': DevelopmentConfig,
                'development': DevelopmentConfig,
                'production': ProductionConfig}
