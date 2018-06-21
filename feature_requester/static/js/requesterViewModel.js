var featureVM = {
    id: null,
    title: null,
    description: null,
    client: {id: 1, name: 'Client A'},
    target_date: null,
    priority: 1,
    product_area: null,
};

featureVM = ko.mapping.fromJS(featureVM);

featureVM.featuresList = ko.observableArray([]);


$(document).ready(function () {
    getFeatures();
    $('#form_save_feature').submit(saveFeature);
});


function getFeatures() {
    $.getJSON('/api/feature', function (data) {
        const features = data.features;
        $.each(features, function (i, item) {
            const vm = ko.mapping.fromJS(item);
            featureVM.featuresList.push(vm);
        });
    }, function (fail) {
        console.log('Fail');
    });
}


function saveFeature(event) {
    event.preventDefault();
    var js = ko.toJS(featureVM);
    delete js.__ko_mapping__;
    delete js.featuresList;
    js.client = {'name': js.client};
    var jsonData = JSON.stringify(js);

    $.ajax({
        url: '/api/feature',
        type: 'POST',
        contentType: "application/json",
        accepts: "application/json",
        dataType: 'json',
        data: jsonData,
        success: function (data) {
            console.log(data);
            const vm = ko.mapping.fromJS(data.feature);
            featureVM.featuresList.unshift(vm);
            $('#new_feature_modal').modal('toggle');
            $('#form_save_feature').trigger('reset');

        },
        error: function (error) {
            console.log("POST error: " + error.status);
        }
    });
}


featureVM.updateFeature = function (request) {
    var num = ko.toJS(request.id);
    console.log(js);
};

featureVM.deleteFeature = function (request) {
    var num = ko.toJS(request.id);
    console.log(js);
};


ko.applyBindings(featureVM);
