function FeatureViewModel() {
    var self = this;

    self.id = ko.observable('');
    self.title = ko.observable('');
    self.description = ko.observable('');
    self.client = ko.observable('');
    self.target_date = ko.observable('');
    self.priority = ko.observable('1');
    self.product_area = ko.observable('');


    var Feature = {
        id: self.id,
        title: self.title,
        description: self.description,
        client: self.client,
        target_date: self.target_date,
        priority: self.priority,
        product_area: self.product_area,
    };


    self.currentFeature = ko.observable(null);


    self.Feature = ko.observable("");
    self.features = ko.observableArray("");


    self.getFeatures = function () {
        $.ajax({
            url: '/api/feature',
            cache: false,
            type: 'GET',
            contentType: "application/json",
            accepts: "application/json",
            data: {},
            success: function (data) {
                self.features(data.features);
            },
            error: function (error) {
                console.log("POST error: " + error.status);
            }
        });
    };


    self.save = function () {
        if (self.Feature.title !== '' && self.Feature.description !== ''
            && self.Feature.client !== '' && self.Feature.product_area !== '') {

            var data = JSON.stringify({
                title: self.title(),
                client: {'name': self.client()},
                description: self.description(),
                target_date: self.target_date(),
                priority: self.priority(),
                product_area: self.product_area()
            });


            $.ajax({
                url: '/api/feature',
                type: 'POST',
                cache: false,
                contentType: "application/json",
                accepts: "application/json",
                dataType: 'json',
                data: data,
                success: function (data) {
                    self.features.unshift(data.feature);
                    self.title = '';
                    self.description = '';
                    self.client = '';
                    self.target_date = '';
                    self.priority = '';
                    self.product_area = '';
                    $('#new_feature_modal').modal('toggle');
                    $('#form_save_feature').trigger('reset');

                },
                error: function (error) {
                    console.log("POST error: " + error.status);
                }
            });
        } else {
            <!-- TODO add error messages -->
            alert('Please add required values!');
        }


    };


    self.updateFeature = function (vm) {
        self.currentFeature(vm);
        $('#update_feature_modal').modal('show');
    };

    self.patchFeature = function (vm) {
        var vm_json = ko.toJS(vm);
        if (vm_json.title !== '' && vm_json.description !== ''
            && vm_json.client !== '' && vm_json.product_area !== '') {
            $.ajax({
                url: 'api/feature/' + vm.id,
                type: 'PATCH',
                cache: false,
                contentType: "application/json",
                accepts: "application/json",
                dataType: 'json',
                data: JSON.stringify({
                    title: vm_json.title,
                    client: vm_json.client,
                    description: vm_json.description,
                    target_date: vm_json.target_date,
                    priority: vm_json.priority,
                    product_area: vm_json.product_area
                }),
                success: function (data) {
                    $('#update_feature_modal').modal('toggle');
                    self.currentFeature(null);
                    self.getFeatures()

                },
                error: function (error) {
                    console.log("PATCH error: " + error.status);
                }
            });
        }
    };


    self.deleteFeature = function (request) {
        var num = ko.toJS(request.id);
        console.log(num);
    };


    self.getFeatures();


}

ko.applyBindings(new FeatureViewModel());