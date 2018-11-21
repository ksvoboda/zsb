django.jQuery(document).ready(function($) {

    var rows = -1;
    var part1 = 'id_pageblock_set-';
    var part2 = '-block_type';
    var counter = 0;
    var selectedDropdown;
    var selectedDropdownValue;
    var selectedText;
    var selectedImage;

    function elementChanged() {
        while (document.getElementById(part1+counter+part2) !== null){
            selectedDropdown = document.getElementById(part1+counter+part2);
            selectedDropdownValue = selectedDropdown.options[selectedDropdown.selectedIndex].value;
            selectedText = document.getElementById('id_pageblock_set-'+counter.toString()+'-block_text').parentElement.parentElement;
            selectedImage = document.getElementById('id_pageblock_set-'+counter.toString()+'-block_image').parentElement.parentElement;

            selectedImage.style.display = 'none';
            selectedText.style.display = 'none';

            if (selectedDropdownValue == 'PIC'){
                selectedImage.style.display = 'block';
            }
            else if (selectedDropdownValue == 'TEXT'){
                selectedText.style.display = 'block';
            }

            counter += 1;
        }
        counter = 0;
    }

    function bindChanges(){
        while (document.getElementById(part1+counter+part2) !== null){
            rows += 1;
            document.getElementById(part1+counter+part2).onchange = function() {elementChanged()};
            counter += 1;
        }
        counter = 0;
    }

    document.getElementById("localized_save_before_reorder_message").value = "Na stránce jsou neuložené změny. Před změnou pořadí je potřeba stránku nejprve uložit.";
    bindChanges();
    elementChanged();

    $(document).on('formset:added', function(event, $row, formsetName) {
        rows += 1;
        document.getElementById(part1+rows+part2).onchange = function() {elementChanged()};
        elementChanged()
    });

    $(document).on('formset:removed', function(event, $row, formsetName) {
        rows -=1;
    });
});