$(function () {
    $('#messages').hide();

});


function FeatureViewModel() {
    var self = this;
    var api_base = 'api/feature';

    //Messages
    var allFieldsMessage = 'All fields are required!';
    var createFeatureMessage = 'Feature created!';
    var somethingWrongMsg = 'Ooops! Something went wrong!';
    var featureUpdatedMsg = 'Feature successfully updated!';

    self.id = ko.observable('');
    self.title = ko.observable('');
    self.description = ko.observable('');
    self.client = ko.observable('');
    self.target_date = ko.observable('');
    self.priority = ko.observable(1);
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
            url: api_base,
            cache: false,
            type: 'GET',
            contentType: "application/json",
            accepts: "application/json",
            data: {},
            success: function (data) {
                self.features(data.features);
            },
            error: function (error) {
                console.log(error.status_code);
                showMessage(somethingWrongMsg + ' Loading features problems!', true);
            }
        });
    };


    self.save = function () {

        if (self.title() !== '' && self.description() !== ''
            && self.client() !== '' && self.product_area() !== ''
            && self.target_date() !== '' && self.priority() !== '') {

            var data = JSON.stringify({
                title: self.title(),
                client: {'name': self.client()},
                description: self.description(),
                target_date: self.target_date(),
                priority: self.priority(),
                product_area: self.product_area()
            });

            $.ajax({
                url: api_base,
                type: 'POST',
                cache: false,
                contentType: "application/json",
                accepts: "application/json",
                dataType: 'json',
                data: data,
                success: function (data) {
                    self.title(null);
                    self.client(null);
                    self.description(null);
                    self.target_date(null);
                    self.priority(1);
                    self.product_area(null);
                    self.getFeatures();
                    $('#new_feature_modal').modal('toggle');
                    $('#form_save_feature').trigger('reset');

                    showMessage(createFeatureMessage, false);

                },
                error: function (error) {
                    showMessage(somethingWrongMsg, true);
                }
            });
        } else {
            showMessage(allFieldsMessage, true);
        }


    };


    self.updateFeature = function (vm) {
        self.currentFeature(vm);
        $('#update_feature_modal').modal('show');
    };

    self.patchFeature = function (vm) {
        var vm_json = ko.toJS(vm);
        if (vm.title !== '' && vm.description !== ''
            && vm.client !== '' && vm.product_area !== ''
            && vm.target_date !== '' && vm.priority !== '') {
            $.ajax({
                url: api_base + '/' + vm.id,
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
                    self.getFeatures();
                    showMessage(featureUpdatedMsg, false);

                },
                error: function (error) {
                    showMessage(somethingWrongMsg, true);
                }
            });
        } else {
            showMessage(allFieldsMessage, true);
        }
    };

    self.openDeleteModal = function (vm) {
        self.currentFeature(vm);
        $('#delete_feature_modal').modal('show');
    };

    self.deleteFeature = function (vm) {
        var vm_json = ko.toJS(vm);
        $.ajax({
            url: api_base + '/' + vm_json.id,
            type: 'DELETE',
            data: {},
            success: function (data) {
                self.features.remove(vm);
                $('#delete_feature_modal').modal('toggle');
                showMessage('Feature ' + vm_json.title + ' deleted!', false);
            }
        });


    };

    self.getFeatures();


}

function showMessage(text, error) {

    var msg_box = $('#messages');
    if (error) {
        msg_box.addClass('alert-warning');
    } else {
        msg_box.addClass('alert-info');
    }

    $('#id_msg_span').text(text);

    msg_box.fadeTo(2000, 1000).slideUp(500, function () {
        msg_box.slideUp(2000);
        msg_box.removeClass('alert-warning');
        msg_box.removeClass('alert-info');
    });
}


ko.applyBindings(new FeatureViewModel());