from ray import serve


@serve.deployment
class MyDeployment:
    def __call__(self, model_path):
        from my_module import my_model

        self.model = my_model.load(model_path)
