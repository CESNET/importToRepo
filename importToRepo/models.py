# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AcceptedOrder(models.Model):
    ordered_by_username_cp = models.TextField(blank=True, null=True)
    selected_alternative_id = models.IntegerField(blank=True, null=True)
    customer_order_date_cp = models.DateTimeField(blank=True, null=True)
    order_cost_centre_cp = models.TextField(blank=True, null=True)
    order_acc_no_cp = models.TextField(blank=True, null=True)
    central_comment = models.TextField(blank=True, null=True)
    order_uid_cp = models.CharField(max_length=128, blank=True, null=True)
    central_order_date = models.DateTimeField(blank=True, null=True)
    supplier_delivery_date = models.DateTimeField(blank=True, null=True)
    customer_delivery_date = models.DateTimeField(blank=True, null=True)
    central_order_status = models.CharField(max_length=18, blank=True, null=True)
    order_comp_id = models.IntegerField(blank=True, null=True)
    history = models.TextField()
    settlement_id = models.IntegerField(blank=True, null=True)
    fixed_costs_share = models.FloatField(blank=True, null=True)
    fixed_costs_share_vat_rate = models.FloatField(blank=True, null=True)
    billing_date = models.DateField(blank=True, null=True)
    vendor_id = models.IntegerField(blank=True, null=True)
    supplier = models.TextField(blank=True, null=True)
    supplier_offer_id = models.IntegerField(blank=True, null=True)
    catno = models.TextField(db_column='catNo', blank=True, null=True)  # Field name made lowercase.
    beautifulcatno = models.TextField(db_column='beautifulCatNo', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    cas_nr = models.TextField(blank=True, null=True)
    package_amount = models.FloatField(blank=True, null=True)
    package_amount_unit = models.TextField(blank=True, null=True)
    number_packages_text = models.TextField(blank=True, null=True)
    density_20 = models.FloatField(blank=True, null=True)
    number_packages = models.FloatField(blank=True, null=True)
    so_price = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    price_currency = models.TextField(blank=True, null=True)
    vat_rate = models.FloatField(blank=True, null=True)
    accepted_order_id = models.AutoField(primary_key=True)
    accepted_order_secret = models.IntegerField(blank=True, null=True)
    accepted_order_created_by = models.TextField(blank=True, null=True)
    accepted_order_created_when = models.DateTimeField(blank=True, null=True)
    accepted_order_created_hashver = models.IntegerField(blank=True, null=True)
    accepted_order_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    accepted_order_changed_by = models.TextField(blank=True, null=True)
    accepted_order_changed_when = models.DateTimeField(blank=True, null=True)
    accepted_order_changed_hashver = models.IntegerField(blank=True, null=True)
    accepted_order_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accepted_order'


class AnalyticalData(models.Model):
    nr_in_reaction = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    molecule_id = models.IntegerField(blank=True, null=True)
    chemical_storage_id = models.IntegerField(blank=True, null=True)
    reaction_id = models.IntegerField(blank=True, null=True)
    reaction_chemical = models.ForeignKey(ReactionChemical, blank=True, null=True)
    fraction_no = models.TextField(blank=True, null=True)
    analytical_data_identifier = models.TextField(blank=True, null=True)
    analytical_data_raw_blob = models.TextField(blank=True, null=True)
    analytical_data_blob = models.TextField(blank=True, null=True)
    measured_by = models.TextField(blank=True, null=True)
    solvent = models.IntegerField(blank=True, null=True)
    analytical_data_interpretation = models.TextField(blank=True, null=True)
    analytical_data_comment = models.TextField(blank=True, null=True)
    analytical_data_properties_blob = models.TextField(blank=True, null=True)
    analytical_data_graphics_blob = models.TextField(blank=True, null=True)
    analytical_data_svg_blob = models.TextField(blank=True, null=True)
    analytical_data_csv = models.TextField(blank=True, null=True)
    analytical_data_graphics_type = models.TextField(blank=True, null=True)
    analytical_data_link_url = models.TextField(blank=True, null=True)
    analytical_data_display_settings = models.IntegerField(blank=True, null=True)
    analytics_method_id = models.IntegerField(blank=True, null=True)
    analytics_method_name = models.TextField(blank=True, null=True)
    analytics_method_text = models.TextField(blank=True, null=True)
    analytics_type_id = models.IntegerField(blank=True, null=True)
    analytics_type_name = models.TextField(blank=True, null=True)
    analytics_type_code = models.TextField(blank=True, null=True)
    analytics_type_text = models.TextField(blank=True, null=True)
    analytics_device_id = models.IntegerField(blank=True, null=True)
    analytics_device_name = models.TextField(blank=True, null=True)
    analytics_device_driver = models.TextField(blank=True, null=True)
    analytical_data_uid = models.CharField(max_length=128, blank=True, null=True)
    analytical_data_ext_archive_id = models.TextField(blank=True, null=True)
    analytical_data_id = models.AutoField(primary_key=True)
    analytical_data_shared = models.IntegerField(blank=True, null=True)
    analytical_data_created_by = models.TextField(blank=True, null=True)
    analytical_data_created_when = models.DateTimeField(blank=True, null=True)
    analytical_data_created_hashver = models.IntegerField(blank=True, null=True)
    analytical_data_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    analytical_data_changed_by = models.TextField(blank=True, null=True)
    analytical_data_changed_when = models.DateTimeField(blank=True, null=True)
    analytical_data_changed_hashver = models.IntegerField(blank=True, null=True)
    analytical_data_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analytical_data'


class AnalyticalDataArchive(models.Model):
    nr_in_reaction = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    molecule_id = models.IntegerField(blank=True, null=True)
    chemical_storage_id = models.IntegerField(blank=True, null=True)
    reaction_id = models.IntegerField(blank=True, null=True)
    reaction_chemical_id = models.IntegerField(blank=True, null=True)
    fraction_no = models.TextField(blank=True, null=True)
    analytical_data_identifier = models.TextField(blank=True, null=True)
    analytical_data_raw_blob = models.TextField(blank=True, null=True)
    analytical_data_blob = models.TextField(blank=True, null=True)
    measured_by = models.TextField(blank=True, null=True)
    solvent = models.IntegerField(blank=True, null=True)
    analytical_data_interpretation = models.TextField(blank=True, null=True)
    analytical_data_comment = models.TextField(blank=True, null=True)
    analytical_data_properties_blob = models.TextField(blank=True, null=True)
    analytical_data_graphics_blob = models.TextField(blank=True, null=True)
    analytical_data_svg_blob = models.TextField(blank=True, null=True)
    analytical_data_csv = models.TextField(blank=True, null=True)
    analytical_data_graphics_type = models.TextField(blank=True, null=True)
    analytical_data_link_url = models.TextField(blank=True, null=True)
    analytical_data_display_settings = models.IntegerField(blank=True, null=True)
    analytics_method_id = models.IntegerField(blank=True, null=True)
    analytics_method_name = models.TextField(blank=True, null=True)
    analytics_method_text = models.TextField(blank=True, null=True)
    analytics_type_id = models.IntegerField(blank=True, null=True)
    analytics_type_name = models.TextField(blank=True, null=True)
    analytics_type_code = models.TextField(blank=True, null=True)
    analytics_type_text = models.TextField(blank=True, null=True)
    analytics_device_id = models.IntegerField(blank=True, null=True)
    analytics_device_name = models.TextField(blank=True, null=True)
    analytics_device_driver = models.TextField(blank=True, null=True)
    analytical_data_uid = models.CharField(max_length=128, blank=True, null=True)
    analytical_data_ext_archive_id = models.TextField(blank=True, null=True)
    analytical_data_id = models.IntegerField(blank=True, null=True)
    analytical_data_shared = models.IntegerField(blank=True, null=True)
    analytical_data_created_by = models.TextField(blank=True, null=True)
    analytical_data_created_when = models.DateTimeField(blank=True, null=True)
    analytical_data_created_hashver = models.IntegerField(blank=True, null=True)
    analytical_data_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    analytical_data_changed_by = models.TextField(blank=True, null=True)
    analytical_data_changed_when = models.DateTimeField(blank=True, null=True)
    analytical_data_changed_hashver = models.IntegerField(blank=True, null=True)
    analytical_data_changed_md5 = models.CharField(max_length=128, blank=True, null=True)
    analytical_data_archive_id = models.AutoField(primary_key=True)
    archive_entity_id = models.IntegerField(blank=True, null=True)
    version_comment = models.TextField(blank=True, null=True)
    is_autosave = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analytical_data_archive'


class AnalyticalDataImage(models.Model):
    analytical_data_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    reaction_id = models.IntegerField(blank=True, null=True)
    image_no = models.IntegerField(blank=True, null=True)
    image_comment = models.TextField(blank=True, null=True)
    analytical_data_graphics_blob = models.TextField(blank=True, null=True)
    analytical_data_svg_blob = models.TextField(blank=True, null=True)
    analytical_data_csv = models.TextField(blank=True, null=True)
    analytical_data_graphics_type = models.TextField(blank=True, null=True)
    analytical_data_display_settings = models.IntegerField(blank=True, null=True)
    analytical_data_image_id = models.AutoField(primary_key=True)
    analytical_data_image_shared = models.IntegerField(blank=True, null=True)
    analytical_data_image_created_by = models.TextField(blank=True, null=True)
    analytical_data_image_created_when = models.DateTimeField(blank=True, null=True)
    analytical_data_image_created_hashver = models.IntegerField(blank=True, null=True)
    analytical_data_image_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    analytical_data_image_changed_by = models.TextField(blank=True, null=True)
    analytical_data_image_changed_when = models.DateTimeField(blank=True, null=True)
    analytical_data_image_changed_hashver = models.IntegerField(blank=True, null=True)
    analytical_data_image_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analytical_data_image'


class AnalyticalDataImageArchive(models.Model):
    analytical_data_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    reaction_id = models.IntegerField(blank=True, null=True)
    image_no = models.IntegerField(blank=True, null=True)
    image_comment = models.TextField(blank=True, null=True)
    analytical_data_graphics_blob = models.TextField(blank=True, null=True)
    analytical_data_svg_blob = models.TextField(blank=True, null=True)
    analytical_data_csv = models.TextField(blank=True, null=True)
    analytical_data_graphics_type = models.TextField(blank=True, null=True)
    analytical_data_display_settings = models.IntegerField(blank=True, null=True)
    analytical_data_image_id = models.IntegerField(blank=True, null=True)
    analytical_data_image_shared = models.IntegerField(blank=True, null=True)
    analytical_data_image_created_by = models.TextField(blank=True, null=True)
    analytical_data_image_created_when = models.DateTimeField(blank=True, null=True)
    analytical_data_image_created_hashver = models.IntegerField(blank=True, null=True)
    analytical_data_image_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    analytical_data_image_changed_by = models.TextField(blank=True, null=True)
    analytical_data_image_changed_when = models.DateTimeField(blank=True, null=True)
    analytical_data_image_changed_hashver = models.IntegerField(blank=True, null=True)
    analytical_data_image_changed_md5 = models.CharField(max_length=128, blank=True, null=True)
    analytical_data_image_archive_id = models.AutoField(primary_key=True)
    archive_entity_id = models.IntegerField(blank=True, null=True)
    version_comment = models.TextField(blank=True, null=True)
    is_autosave = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analytical_data_image_archive'


class AnalyticsDevice(models.Model):
    analytics_device_name = models.TextField(blank=True, null=True)
    analytics_device_driver = models.TextField(blank=True, null=True)
    analytics_type_id = models.IntegerField(blank=True, null=True)
    analytics_device_url = models.TextField(blank=True, null=True)
    analytics_device_username = models.TextField(blank=True, null=True)
    analytics_device_password = models.TextField(blank=True, null=True)
    analytics_device_default_permission = models.CharField(max_length=9, blank=True, null=True)
    analytics_device_options = models.TextField(blank=True, null=True)
    analytics_device_id = models.AutoField(primary_key=True)
    analytics_device_disabled = models.IntegerField(blank=True, null=True)
    analytics_device_created_by = models.TextField(blank=True, null=True)
    analytics_device_created_when = models.DateTimeField(blank=True, null=True)
    analytics_device_created_hashver = models.IntegerField(blank=True, null=True)
    analytics_device_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    analytics_device_changed_by = models.TextField(blank=True, null=True)
    analytics_device_changed_when = models.DateTimeField(blank=True, null=True)
    analytics_device_changed_hashver = models.IntegerField(blank=True, null=True)
    analytics_device_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analytics_device'


class AnalyticsDevicePermission(models.Model):
    analytics_device_id = models.IntegerField(blank=True, null=True)
    person_id = models.IntegerField(blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    analytics_device_permission_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'analytics_device_permission'


class AnalyticsMethod(models.Model):
    analytics_method_name = models.TextField(blank=True, null=True)
    analytics_method_text = models.TextField(blank=True, null=True)
    analytics_type_id = models.IntegerField(blank=True, null=True)
    analytics_device_id = models.IntegerField(blank=True, null=True)
    analytics_device_options = models.TextField(blank=True, null=True)
    analytics_method_id = models.AutoField(primary_key=True)
    analytics_method_disabled = models.IntegerField(blank=True, null=True)
    analytics_method_created_by = models.TextField(blank=True, null=True)
    analytics_method_created_when = models.DateTimeField(blank=True, null=True)
    analytics_method_created_hashver = models.IntegerField(blank=True, null=True)
    analytics_method_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    analytics_method_changed_by = models.TextField(blank=True, null=True)
    analytics_method_changed_when = models.DateTimeField(blank=True, null=True)
    analytics_method_changed_hashver = models.IntegerField(blank=True, null=True)
    analytics_method_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analytics_method'


class AnalyticsType(models.Model):
    analytics_type_name = models.TextField(blank=True, null=True)
    analytics_type_code = models.TextField(blank=True, null=True)
    analytics_type_text = models.TextField(blank=True, null=True)
    priority = models.SmallIntegerField(blank=True, null=True)
    analytics_type_id = models.AutoField(primary_key=True)
    analytics_type_created_by = models.TextField(blank=True, null=True)
    analytics_type_created_when = models.DateTimeField(blank=True, null=True)
    analytics_type_created_hashver = models.IntegerField(blank=True, null=True)
    analytics_type_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    analytics_type_changed_by = models.TextField(blank=True, null=True)
    analytics_type_changed_when = models.DateTimeField(blank=True, null=True)
    analytics_type_changed_hashver = models.IntegerField(blank=True, null=True)
    analytics_type_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analytics_type'


class Author(models.Model):
    literature_id = models.IntegerField(blank=True, null=True)
    nr_in_literature = models.IntegerField(blank=True, null=True)
    author_last = models.TextField(blank=True, null=True)
    author_first = models.TextField(blank=True, null=True)
    author_type = models.SmallIntegerField(blank=True, null=True)
    author_id = models.AutoField(primary_key=True)
    author_shared = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author'


class Cache(models.Model):
    person_id = models.IntegerField(blank=True, null=True)
    cache_sess_id = models.TextField(blank=True, null=True)
    query_md5 = models.CharField(max_length=16, blank=True, null=True)
    created = models.IntegerField(blank=True, null=True)
    last_update = models.IntegerField(blank=True, null=True)
    cache_blob = models.TextField(blank=True, null=True)
    cache_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cache'


class ChangeNotify(models.Model):
    for_table = models.TextField(blank=True, null=True)
    parent_key = models.IntegerField(db_column='pk', blank=True, null=True)
    made_when = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_notify'


class ChemicalOrder(models.Model):
    ordered_by_person = models.IntegerField(blank=True, null=True)
    ordered_by_username = models.TextField(blank=True, null=True)
    customer_selected_alternative_id = models.IntegerField(blank=True, null=True)
    customer_order_date = models.DateTimeField(blank=True, null=True)
    order_cost_centre = models.TextField(blank=True, null=True)
    order_acc_no = models.TextField(blank=True, null=True)
    customer_comment = models.TextField(blank=True, null=True)
    customer_order_status = models.CharField(max_length=18, blank=True, null=True)
    may_change_supplier = models.CharField(max_length=16, blank=True, null=True)
    order_uid = models.CharField(max_length=128, blank=True, null=True)
    chemical_storage_id = models.IntegerField(blank=True, null=True)
    chemical_order_id = models.AutoField(primary_key=True)
    chemical_order_secret = models.IntegerField(blank=True, null=True)
    chemical_order_created_by = models.TextField(blank=True, null=True)
    chemical_order_created_when = models.DateTimeField(blank=True, null=True)
    chemical_order_created_hashver = models.IntegerField(blank=True, null=True)
    chemical_order_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    chemical_order_changed_by = models.TextField(blank=True, null=True)
    chemical_order_changed_when = models.DateTimeField(blank=True, null=True)
    chemical_order_changed_hashver = models.IntegerField(blank=True, null=True)
    chemical_order_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chemical_order'


class ChemicalStorage(models.Model):
    molecule_id = models.IntegerField(blank=True, null=True)
    from_reaction_id = models.IntegerField(blank=True, null=True)
    from_reaction_chemical_id = models.IntegerField(blank=True, null=True)
    chemical_order_id = models.IntegerField(blank=True, null=True)
    purity = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    open_date = models.DateField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    actual_amount = models.FloatField(blank=True, null=True)
    amount_unit = models.TextField(blank=True, null=True)
    amount_is_volume = models.IntegerField(blank=True, null=True)
    warn_level = models.FloatField(blank=True, null=True)
    tmd = models.FloatField(blank=True, null=True)
    tmd_unit = models.TextField(blank=True, null=True)
    chemical_storage_bilancing = models.IntegerField(blank=True, null=True)
    chemical_storage_attrib = models.CharField(max_length=96, blank=True, null=True)
    chemical_storage_conc = models.FloatField(blank=True, null=True)
    chemical_storage_conc_unit = models.TextField(blank=True, null=True)
    chemical_storage_solvent = models.TextField(blank=True, null=True)
    chemical_storage_density_20 = models.FloatField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    owner_person_id = models.IntegerField(blank=True, null=True)
    container = models.TextField(blank=True, null=True)
    cat_no = models.TextField(blank=True, null=True)
    lot_no = models.TextField(blank=True, null=True)
    protection_gas = models.TextField(blank=True, null=True)
    disposed_when = models.DateField(blank=True, null=True)
    disposed_by = models.TextField(blank=True, null=True)
    storage_id = models.IntegerField(blank=True, null=True)
    compartment = models.TextField(blank=True, null=True)
    transferred_to_db_id = models.IntegerField(blank=True, null=True)
    borrowed_by_db_id = models.IntegerField(blank=True, null=True)
    borrowed_by_person_id = models.IntegerField(blank=True, null=True)
    borrowed_when = models.DateTimeField(blank=True, null=True)
    comment_cheminstor = models.TextField(blank=True, null=True)
    history = models.TextField()
    migrate_id_cheminstor = models.TextField(blank=True, null=True)
    chemical_storage_btm_list = models.IntegerField(blank=True, null=True)
    chemical_storage_sprengg_list = models.TextField(blank=True, null=True)
    safety_sheet_blob = models.TextField(blank=True, null=True)
    safety_sheet_url = models.TextField(blank=True, null=True)
    safety_sheet_mime = models.TextField(blank=True, null=True)
    safety_sheet_by = models.TextField(blank=True, null=True)
    alt_safety_sheet_blob = models.TextField(blank=True, null=True)
    alt_safety_sheet_url = models.TextField(blank=True, null=True)
    alt_safety_sheet_mime = models.TextField(blank=True, null=True)
    alt_safety_sheet_by = models.TextField(blank=True, null=True)
    inventory_check_by = models.TextField(blank=True, null=True)
    inventory_check_when = models.DateTimeField(blank=True, null=True)
    supplier = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    price_currency = models.TextField(blank=True, null=True)
    chemical_storage_id = models.AutoField(primary_key=True)
    chemical_storage_user0 = models.TextField(blank=True, null=True)
    chemical_storage_user1 = models.TextField(blank=True, null=True)
    chemical_storage_user2 = models.TextField(blank=True, null=True)
    chemical_storage_user3 = models.TextField(blank=True, null=True)
    chemical_storage_int0 = models.IntegerField(blank=True, null=True)
    chemical_storage_int1 = models.IntegerField(blank=True, null=True)
    chemical_storage_dbl0 = models.FloatField(blank=True, null=True)
    chemical_storage_dbl1 = models.FloatField(blank=True, null=True)
    chemical_storage_secret = models.IntegerField(blank=True, null=True)
    chemical_storage_disabled = models.IntegerField(blank=True, null=True)
    chemical_storage_created_by = models.TextField(blank=True, null=True)
    chemical_storage_created_when = models.DateTimeField(blank=True, null=True)
    chemical_storage_created_hashver = models.IntegerField(blank=True, null=True)
    chemical_storage_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    chemical_storage_changed_by = models.TextField(blank=True, null=True)
    chemical_storage_changed_when = models.DateTimeField(blank=True, null=True)
    chemical_storage_changed_hashver = models.IntegerField(blank=True, null=True)
    chemical_storage_changed_md5 = models.CharField(max_length=128, blank=True, null=True)
    chemical_storage_barcode = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chemical_storage'


class ChemicalStorageArchive(models.Model):
    molecule_id = models.IntegerField(blank=True, null=True)
    from_reaction_id = models.IntegerField(blank=True, null=True)
    from_reaction_chemical_id = models.IntegerField(blank=True, null=True)
    chemical_order_id = models.IntegerField(blank=True, null=True)
    purity = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    open_date = models.DateField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    actual_amount = models.FloatField(blank=True, null=True)
    amount_unit = models.TextField(blank=True, null=True)
    amount_is_volume = models.IntegerField(blank=True, null=True)
    warn_level = models.FloatField(blank=True, null=True)
    tmd = models.FloatField(blank=True, null=True)
    tmd_unit = models.TextField(blank=True, null=True)
    chemical_storage_bilancing = models.IntegerField(blank=True, null=True)
    chemical_storage_attrib = models.CharField(max_length=96, blank=True, null=True)
    chemical_storage_conc = models.FloatField(blank=True, null=True)
    chemical_storage_conc_unit = models.TextField(blank=True, null=True)
    chemical_storage_solvent = models.TextField(blank=True, null=True)
    chemical_storage_density_20 = models.FloatField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    owner_person_id = models.IntegerField(blank=True, null=True)
    container = models.TextField(blank=True, null=True)
    cat_no = models.TextField(blank=True, null=True)
    lot_no = models.TextField(blank=True, null=True)
    protection_gas = models.TextField(blank=True, null=True)
    disposed_when = models.DateField(blank=True, null=True)
    disposed_by = models.TextField(blank=True, null=True)
    storage_id = models.IntegerField(blank=True, null=True)
    compartment = models.TextField(blank=True, null=True)
    transferred_to_db_id = models.IntegerField(blank=True, null=True)
    borrowed_by_db_id = models.IntegerField(blank=True, null=True)
    borrowed_by_person_id = models.IntegerField(blank=True, null=True)
    borrowed_when = models.DateTimeField(blank=True, null=True)
    comment_cheminstor = models.TextField(blank=True, null=True)
    history = models.TextField()
    migrate_id_cheminstor = models.TextField(blank=True, null=True)
    chemical_storage_btm_list = models.IntegerField(blank=True, null=True)
    chemical_storage_sprengg_list = models.TextField(blank=True, null=True)
    safety_sheet_blob = models.TextField(blank=True, null=True)
    safety_sheet_url = models.TextField(blank=True, null=True)
    safety_sheet_mime = models.TextField(blank=True, null=True)
    safety_sheet_by = models.TextField(blank=True, null=True)
    alt_safety_sheet_blob = models.TextField(blank=True, null=True)
    alt_safety_sheet_url = models.TextField(blank=True, null=True)
    alt_safety_sheet_mime = models.TextField(blank=True, null=True)
    alt_safety_sheet_by = models.TextField(blank=True, null=True)
    inventory_check_by = models.TextField(blank=True, null=True)
    inventory_check_when = models.DateTimeField(blank=True, null=True)
    supplier = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    price_currency = models.TextField(blank=True, null=True)
    chemical_storage_id = models.IntegerField(blank=True, null=True)
    chemical_storage_user0 = models.TextField(blank=True, null=True)
    chemical_storage_user1 = models.TextField(blank=True, null=True)
    chemical_storage_user2 = models.TextField(blank=True, null=True)
    chemical_storage_user3 = models.TextField(blank=True, null=True)
    chemical_storage_int0 = models.IntegerField(blank=True, null=True)
    chemical_storage_int1 = models.IntegerField(blank=True, null=True)
    chemical_storage_dbl0 = models.FloatField(blank=True, null=True)
    chemical_storage_dbl1 = models.FloatField(blank=True, null=True)
    chemical_storage_secret = models.IntegerField(blank=True, null=True)
    chemical_storage_disabled = models.IntegerField(blank=True, null=True)
    chemical_storage_created_by = models.TextField(blank=True, null=True)
    chemical_storage_created_when = models.DateTimeField(blank=True, null=True)
    chemical_storage_created_hashver = models.IntegerField(blank=True, null=True)
    chemical_storage_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    chemical_storage_changed_by = models.TextField(blank=True, null=True)
    chemical_storage_changed_when = models.DateTimeField(blank=True, null=True)
    chemical_storage_changed_hashver = models.IntegerField(blank=True, null=True)
    chemical_storage_changed_md5 = models.CharField(max_length=128, blank=True, null=True)
    chemical_storage_barcode = models.CharField(max_length=20, blank=True, null=True)
    chemical_storage_archive_id = models.AutoField(primary_key=True)
    archive_entity_id = models.IntegerField(blank=True, null=True)
    version_comment = models.TextField(blank=True, null=True)
    is_autosave = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chemical_storage_archive'


class ChemicalStorageChemicalStorageType(models.Model):
    chemical_storage_id = models.IntegerField(blank=True, null=True)
    chemical_storage_type_id = models.IntegerField(blank=True, null=True)
    chemical_storage_chemical_storage_type_id = models.AutoField(primary_key=True)
    chemical_storage_chemical_storage_type_secret = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chemical_storage_chemical_storage_type'


class ChemicalStorageLiterature(models.Model):
    chemical_storage_id = models.IntegerField(blank=True, null=True)
    literature_id = models.IntegerField(blank=True, null=True)
    chemical_storage_literature_id = models.AutoField(primary_key=True)
    chemical_storage_literature_secret = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chemical_storage_literature'


class ChemicalStorageLiteratureArchive(models.Model):
    chemical_storage_id = models.IntegerField(blank=True, null=True)
    literature_id = models.IntegerField(blank=True, null=True)
    chemical_storage_literature_id = models.IntegerField(blank=True, null=True)
    chemical_storage_literature_secret = models.IntegerField(blank=True, null=True)
    chemical_storage_literature_archive_id = models.AutoField(primary_key=True)
    archive_entity_id = models.IntegerField(blank=True, null=True)
    version_comment = models.TextField(blank=True, null=True)
    is_autosave = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chemical_storage_literature_archive'


class ChemicalStorageProperty(models.Model):
    chemical_storage_id = models.IntegerField(blank=True, null=True)
    chemical_storage_property_name = models.TextField(blank=True, null=True)
    chemical_storage_property_value = models.TextField(blank=True, null=True)
    chemical_storage_property_number = models.FloatField(blank=True, null=True)
    chemical_storage_property_id = models.AutoField(primary_key=True)
    chemical_storage_property_secret = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chemical_storage_property'


class ChemicalStorageType(models.Model):
    chemical_storage_type_name = models.TextField(blank=True, null=True)
    chemical_storage_type_text = models.TextField(blank=True, null=True)
    chemical_storage_type_id = models.AutoField(primary_key=True)
    chemical_storage_type_secret = models.IntegerField(blank=True, null=True)
    chemical_storage_type_created_by = models.TextField(blank=True, null=True)
    chemical_storage_type_created_when = models.DateTimeField(blank=True, null=True)
    chemical_storage_type_created_hashver = models.IntegerField(blank=True, null=True)
    chemical_storage_type_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    chemical_storage_type_changed_by = models.TextField(blank=True, null=True)
    chemical_storage_type_changed_when = models.DateTimeField(blank=True, null=True)
    chemical_storage_type_changed_hashver = models.IntegerField(blank=True, null=True)
    chemical_storage_type_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chemical_storage_type'


class Class(models.Model):
    class_name = models.TextField(blank=True, null=True)
    default_unit = models.TextField(blank=True, null=True)
    class_type = models.TextField(blank=True, null=True)
    class_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'class'


class CostCentre(models.Model):
    cost_centre = models.CharField(unique=True, max_length=32, blank=True, null=True)
    acc_no = models.TextField(blank=True, null=True)
    cost_centre_name = models.TextField(blank=True, null=True)
    cost_centre_id = models.AutoField(primary_key=True)
    cost_centre_secret = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_centre'


class DbInfo(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    value = models.TextField(blank=True, null=True)
    db_info_secret = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_info'


class GcPeak(models.Model):
    analytical_data_id = models.IntegerField(blank=True, null=True)
    reaction_id = models.IntegerField(blank=True, null=True)
    reaction_chemical_id = models.IntegerField(blank=True, null=True)
    retention_time = models.FloatField(blank=True, null=True)
    area_percent = models.FloatField(blank=True, null=True)
    gc_peak_comment = models.TextField(blank=True, null=True)
    gc_yield = models.FloatField(blank=True, null=True)
    response_factor = models.FloatField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    gc_peak_id = models.AutoField(primary_key=True)
    gc_peak_shared = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gc_peak'


class GcPeakArchive(models.Model):
    analytical_data_id = models.IntegerField(blank=True, null=True)
    reaction_id = models.IntegerField(blank=True, null=True)
    reaction_chemical_id = models.IntegerField(blank=True, null=True)
    retention_time = models.FloatField(blank=True, null=True)
    area_percent = models.FloatField(blank=True, null=True)
    gc_peak_comment = models.TextField(blank=True, null=True)
    gc_yield = models.FloatField(blank=True, null=True)
    response_factor = models.FloatField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    gc_peak_id = models.IntegerField(blank=True, null=True)
    gc_peak_shared = models.IntegerField(blank=True, null=True)
    gc_peak_archive_id = models.AutoField(primary_key=True)
    archive_entity_id = models.IntegerField(blank=True, null=True)
    version_comment = models.TextField(blank=True, null=True)
    is_autosave = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gc_peak_archive'


class GlobalSettings(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_settings'


class Institution(models.Model):
    institution_name = models.TextField(blank=True, null=True)
    person_name = models.TextField(blank=True, null=True)
    department_name = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    postcode = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    street_number = models.SmallIntegerField(blank=True, null=True)
    tel_no = models.TextField(blank=True, null=True)
    fax_no = models.TextField(blank=True, null=True)
    customer_id = models.TextField(blank=True, null=True)
    institution_type = models.CharField(max_length=32, blank=True, null=True)
    comment_institution = models.TextField(blank=True, null=True)
    institution_id = models.AutoField(primary_key=True)
    institution_created_by = models.TextField(blank=True, null=True)
    institution_created_when = models.DateTimeField(blank=True, null=True)
    institution_created_hashver = models.IntegerField(blank=True, null=True)
    institution_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    institution_changed_by = models.TextField(blank=True, null=True)
    institution_changed_when = models.DateTimeField(blank=True, null=True)
    institution_changed_hashver = models.IntegerField(blank=True, null=True)
    institution_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institution'


class InstitutionCode(models.Model):
    institution_id = models.IntegerField(blank=True, null=True)
    supplier_code = models.TextField(blank=True, null=True)
    institution_code_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'institution_code'


class Person(models.Model):
    last_name = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    nee = models.TextField(blank=True, null=True)
    sigle = models.TextField(blank=True, null=True)
    remote_host = models.TextField(blank=True, null=True)
    supervisor_id = models.IntegerField(blank=True, null=True)
    institution_id = models.IntegerField(blank=True, null=True)
    permissions = models.IntegerField(blank=True, null=True)
    predefined_permissions_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=32, blank=True, null=True)
    preferred_language = models.TextField(blank=True, null=True)
    cost_centre = models.TextField(blank=True, null=True)
    acc_no = models.TextField(blank=True, null=True)
    cost_limit = models.FloatField(blank=True, null=True)
    cost_limit_currency = models.TextField(blank=True, null=True)
    preferences = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    email_chemical_supply = models.TextField(blank=True, null=True)
    person_id = models.AutoField(primary_key=True)
    person_secret = models.IntegerField(blank=True, null=True)
    person_disabled = models.IntegerField(blank=True, null=True)
    person_created_by = models.TextField(blank=True, null=True)
    person_created_when = models.DateTimeField(blank=True, null=True)
    person_created_hashver = models.IntegerField(blank=True, null=True)
    person_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    person_changed_by = models.TextField(blank=True, null=True)
    person_changed_when = models.DateTimeField(blank=True, null=True)
    person_changed_hashver = models.IntegerField(blank=True, null=True)
    person_changed_md5 = models.CharField(max_length=128, blank=True, null=True)
    person_barcode = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class LabJournal(models.Model):
    person = models.ForeignKey(Person, blank=True, null=True)
    lab_journal_code = models.CharField(unique=True, max_length=32, blank=True, null=True)
    lab_journal_status = models.CharField(max_length=7, blank=True, null=True)
    default_copy_target = models.IntegerField(blank=True, null=True)
    default_permissions = models.IntegerField(blank=True, null=True)
    lab_journal_uid = models.CharField(max_length=128, blank=True, null=True)
    lab_journal_id = models.AutoField(primary_key=True)
    lab_journal_disabled = models.IntegerField(blank=True, null=True)
    lab_journal_created_by = models.TextField(blank=True, null=True)
    lab_journal_created_when = models.DateTimeField(blank=True, null=True)
    lab_journal_created_hashver = models.IntegerField(blank=True, null=True)
    lab_journal_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    lab_journal_changed_by = models.TextField(blank=True, null=True)
    lab_journal_changed_when = models.DateTimeField(blank=True, null=True)
    lab_journal_changed_hashver = models.IntegerField(blank=True, null=True)
    lab_journal_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_journal'


class LabJournalPerson(models.Model):
    lab_journal_id = models.IntegerField(blank=True, null=True)
    person_id = models.IntegerField(blank=True, null=True)
    permissions = models.IntegerField(blank=True, null=True)
    lab_journal_person_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'lab_journal_person'


class Literature(models.Model):
    sci_journal_id = models.IntegerField(blank=True, null=True)
    literature_year = models.SmallIntegerField(blank=True, null=True)
    literature_volume = models.SmallIntegerField(blank=True, null=True)
    issue = models.SmallIntegerField(blank=True, null=True)
    page_low = models.SmallIntegerField(blank=True, null=True)
    page_high = models.SmallIntegerField(blank=True, null=True)
    literature_blob = models.TextField(blank=True, null=True)
    literature_blob_fulltext = models.TextField(blank=True, null=True)
    literature_mime = models.TextField(blank=True, null=True)
    literature_graphics_blob = models.TextField(blank=True, null=True)
    literature_graphics_type = models.TextField(blank=True, null=True)
    doi = models.TextField(blank=True, null=True)
    isbn = models.TextField(blank=True, null=True)
    literature_title = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    edition = models.SmallIntegerField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    language_code = models.TextField(blank=True, null=True)
    literature_type = models.SmallIntegerField(blank=True, null=True)
    literature_group = models.IntegerField(blank=True, null=True)
    literature_id = models.AutoField(primary_key=True)
    literature_shared = models.IntegerField(blank=True, null=True)
    literature_created_by = models.TextField(blank=True, null=True)
    literature_created_when = models.DateTimeField(blank=True, null=True)
    literature_created_hashver = models.IntegerField(blank=True, null=True)
    literature_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    literature_changed_by = models.TextField(blank=True, null=True)
    literature_changed_when = models.DateTimeField(blank=True, null=True)
    literature_changed_hashver = models.IntegerField(blank=True, null=True)
    literature_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'literature'


class LockTable(models.Model):
    for_table = models.TextField(blank=True, null=True)
    parent_key = models.IntegerField(db_column='pk', blank=True, null=True)
    locked_by = models.TextField(blank=True, null=True)
    locked_sess_id = models.TextField(blank=True, null=True)
    locked_when = models.DateTimeField(blank=True, null=True)
    locked_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lock_table'
        unique_together = (('for_table', 'parent_key'),)


class MatStammNr(models.Model):
    molecule_id = models.IntegerField(blank=True, null=True)
    sap_stamm_nr = models.CharField(unique=True, max_length=32, blank=True, null=True)
    comment_stamm_nr = models.TextField(blank=True, null=True)
    mat_stamm_nr_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'mat_stamm_nr'


class Message(models.Model):
    from_person = models.IntegerField(blank=True, null=True)
    issued = models.DateTimeField(blank=True, null=True)
    message_subject = models.TextField(blank=True, null=True)
    message_text = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=6, blank=True, null=True)
    do_until = models.DateField(blank=True, null=True)
    every_xx_interval = models.IntegerField(blank=True, null=True)
    interval_unit = models.CharField(max_length=5, blank=True, null=True)
    message_id = models.AutoField(primary_key=True)
    message_created_by = models.TextField(blank=True, null=True)
    message_created_when = models.DateTimeField(blank=True, null=True)
    message_created_hashver = models.IntegerField(blank=True, null=True)
    message_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    message_changed_by = models.TextField(blank=True, null=True)
    message_changed_when = models.DateTimeField(blank=True, null=True)
    message_changed_hashver = models.IntegerField(blank=True, null=True)
    message_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class MessagePerson(models.Model):
    message_id = models.IntegerField(blank=True, null=True)
    person_id = models.IntegerField(blank=True, null=True)
    completion_status = models.CharField(max_length=11, blank=True, null=True)
    p_comment = models.TextField(blank=True, null=True)
    message_person_id = models.AutoField(primary_key=True)
    message_person_created_by = models.TextField(blank=True, null=True)
    message_person_created_when = models.DateTimeField(blank=True, null=True)
    message_person_created_hashver = models.IntegerField(blank=True, null=True)
    message_person_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    message_person_changed_by = models.TextField(blank=True, null=True)
    message_person_changed_when = models.DateTimeField(blank=True, null=True)
    message_person_changed_hashver = models.IntegerField(blank=True, null=True)
    message_person_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_person'


class Molecule(models.Model):
    cas_nr = models.TextField(blank=True, null=True)
    smiles = models.TextField(blank=True, null=True)
    smiles_stereo = models.TextField(blank=True, null=True)
    inchi = models.TextField(blank=True, null=True)
    molfile_blob = models.BinaryField(blank=True, null=True)
    molecule_serialized = models.BinaryField(blank=True, null=True)
    molfile_blob_source = models.TextField(blank=True, null=True)
    emp_formula = models.TextField(blank=True, null=True)
    emp_formula_sort = models.TextField(blank=True, null=True)
    emp_formula_source = models.TextField(blank=True, null=True)
    mw = models.FloatField(blank=True, null=True)
    mw_monoiso = models.FloatField(blank=True, null=True)
    rdb = models.FloatField(blank=True, null=True)
    mw_source = models.TextField(blank=True, null=True)
    density_20 = models.FloatField(blank=True, null=True)
    density_20_source = models.TextField(blank=True, null=True)
    molecule_bilancing = models.IntegerField(blank=True, null=True)
    default_warn_level = models.FloatField(blank=True, null=True)
    n_20 = models.FloatField(blank=True, null=True)
    n_20_source = models.TextField(blank=True, null=True)
    mp_low = models.FloatField(blank=True, null=True)
    mp_high = models.FloatField(blank=True, null=True)
    mp_source = models.TextField(blank=True, null=True)
    bp_low = models.FloatField(blank=True, null=True)
    bp_high = models.FloatField(blank=True, null=True)
    bp_press = models.FloatField(blank=True, null=True)
    press_unit = models.TextField(blank=True, null=True)
    bp_source = models.TextField(blank=True, null=True)
    safety_r = models.TextField(blank=True, null=True)
    safety_h = models.TextField(blank=True, null=True)
    safety_s = models.TextField(blank=True, null=True)
    safety_p = models.TextField(blank=True, null=True)
    safety_text = models.TextField(blank=True, null=True)
    safety_sym = models.TextField(blank=True, null=True)
    safety_sym_ghs = models.TextField(blank=True, null=True)
    safety_source = models.TextField(blank=True, null=True)
    gif_file = models.BinaryField(blank=True, null=True)
    svg_file = models.BinaryField(blank=True, null=True)
    comment_mol = models.TextField(blank=True, null=True)
    migrate_id_mol = models.TextField(blank=True, null=True)
    safety_cancer = models.TextField(blank=True, null=True)
    safety_mutagen = models.TextField(blank=True, null=True)
    safety_reprod = models.TextField(blank=True, null=True)
    safety_wgk = models.TextField(blank=True, null=True)
    safety_danger = models.TextField(blank=True, null=True)
    molecule_btm_list = models.IntegerField(blank=True, null=True)
    molecule_sprengg_list = models.TextField(blank=True, null=True)
    default_safety_sheet_blob = models.BinaryField(blank=True, null=True)
    default_safety_sheet_url = models.TextField(blank=True, null=True)
    default_safety_sheet_mime = models.TextField(blank=True, null=True)
    default_safety_sheet_by = models.TextField(blank=True, null=True)
    alt_default_safety_sheet_blob = models.TextField(blank=True, null=True)
    alt_default_safety_sheet_url = models.TextField(blank=True, null=True)
    alt_default_safety_sheet_mime = models.TextField(blank=True, null=True)
    alt_default_safety_sheet_by = models.TextField(blank=True, null=True)
    pos_liste = models.IntegerField(blank=True, null=True)
    neg_liste = models.IntegerField(blank=True, null=True)
    molecule_id = models.AutoField(primary_key=True)
    fingerprint1 = models.IntegerField()
    fingerprint2 = models.IntegerField()
    fingerprint3 = models.IntegerField()
    fingerprint4 = models.IntegerField()
    fingerprint5 = models.IntegerField()
    fingerprint6 = models.IntegerField()
    fingerprint7 = models.IntegerField()
    fingerprint8 = models.IntegerField()
    fingerprint9 = models.IntegerField()
    fingerprint10 = models.IntegerField()
    fingerprint11 = models.IntegerField()
    fingerprint12 = models.IntegerField()
    fingerprint13 = models.IntegerField()
    fingerprint14 = models.IntegerField()
    fingerprint15 = models.IntegerField()
    fingerprint16 = models.IntegerField()
    molecule_user0 = models.TextField(blank=True, null=True)
    molecule_user1 = models.TextField(blank=True, null=True)
    molecule_user2 = models.TextField(blank=True, null=True)
    molecule_user3 = models.TextField(blank=True, null=True)
    molecule_user4 = models.TextField(blank=True, null=True)
    molecule_user5 = models.TextField(blank=True, null=True)
    molecule_user6 = models.TextField(blank=True, null=True)
    molecule_user7 = models.TextField(blank=True, null=True)
    molecule_int0 = models.IntegerField(blank=True, null=True)
    molecule_int1 = models.IntegerField(blank=True, null=True)
    molecule_dbl0 = models.FloatField(blank=True, null=True)
    molecule_dbl1 = models.FloatField(blank=True, null=True)
    molecule_secret = models.IntegerField(blank=True, null=True)
    molecule_created_by = models.TextField(blank=True, null=True)
    molecule_created_when = models.DateTimeField(blank=True, null=True)
    molecule_created_hashver = models.IntegerField(blank=True, null=True)
    molecule_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    molecule_changed_by = models.TextField(blank=True, null=True)
    molecule_changed_when = models.DateTimeField(blank=True, null=True)
    molecule_changed_hashver = models.IntegerField(blank=True, null=True)
    molecule_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'molecule'


class MoleculeInstructions(models.Model):
    molecule_id = models.IntegerField(blank=True, null=True)
    lang = models.TextField(blank=True, null=True)
    file_blob = models.TextField(blank=True, null=True)
    file_image = models.TextField(blank=True, null=True)
    betr_anw_gefahren = models.TextField(blank=True, null=True)
    betr_anw_schutzmass = models.TextField(blank=True, null=True)
    betr_anw_schutzmass_sym = models.TextField(blank=True, null=True)
    betr_anw_verhalten = models.TextField(blank=True, null=True)
    betr_anw_verhalten_sym = models.TextField(blank=True, null=True)
    betr_anw_erste_h = models.TextField(blank=True, null=True)
    betr_anw_erste_h_sym = models.TextField(blank=True, null=True)
    betr_anw_entsorgung = models.TextField(blank=True, null=True)
    molecule_instructions_comment = models.TextField(blank=True, null=True)
    molecule_instructions_id = models.AutoField(primary_key=True)
    molecule_instructions_secret = models.IntegerField(blank=True, null=True)
    molecule_instructions_created_by = models.TextField(blank=True, null=True)
    molecule_instructions_created_when = models.DateTimeField(blank=True, null=True)
    molecule_instructions_created_hashver = models.IntegerField(blank=True, null=True)
    molecule_instructions_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    molecule_instructions_changed_by = models.TextField(blank=True, null=True)
    molecule_instructions_changed_when = models.DateTimeField(blank=True, null=True)
    molecule_instructions_changed_hashver = models.IntegerField(blank=True, null=True)
    molecule_instructions_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'molecule_instructions'


class MoleculeLiterature(models.Model):
    molecule_id = models.IntegerField(blank=True, null=True)
    literature_id = models.IntegerField(blank=True, null=True)
    molecule_literature_id = models.AutoField(primary_key=True)
    molecule_literature_secret = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'molecule_literature'


class MoleculeMoleculeType(models.Model):
    molecule_id = models.IntegerField(blank=True, null=True)
    molecule_type_id = models.IntegerField(blank=True, null=True)
    molecule_molecule_type_id = models.AutoField(primary_key=True)
    molecule_molecule_type_secret = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'molecule_molecule_type'


class MoleculeNames(models.Model):
    molecule_id = models.IntegerField(blank=True, null=True)
    molecule_name = models.TextField(blank=True, null=True)
    language_id = models.TextField(blank=True, null=True)
    is_trivial_name = models.SmallIntegerField(blank=True, null=True)
    is_standard = models.IntegerField(blank=True, null=True)
    molecule_names_id = models.AutoField(primary_key=True)
    molecule_names_secret = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'molecule_names'


class MoleculeProperty(models.Model):
    molecule_id = models.IntegerField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)
    # Field renamed because it was a Python reserved word.
    value_low = models.FloatField(blank=True, null=True)
    value_high = models.FloatField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    molecule_property_comment = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    analytical_data_graphics_blob = models.TextField(blank=True, null=True)
    analytical_data_svg_blob = models.TextField(blank=True, null=True)
    acquired = models.CharField(max_length=13, blank=True, null=True)
    molecule_property_id = models.AutoField(primary_key=True)
    molecule_property_secret = models.IntegerField(blank=True, null=True)
    molecule_property_created_by = models.TextField(blank=True, null=True)
    molecule_property_created_when = models.DateTimeField(blank=True, null=True)
    molecule_property_created_hashver = models.IntegerField(blank=True, null=True)
    molecule_property_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    molecule_property_changed_by = models.TextField(blank=True, null=True)
    molecule_property_changed_when = models.DateTimeField(blank=True, null=True)
    molecule_property_changed_hashver = models.IntegerField(blank=True, null=True)
    molecule_property_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'molecule_property'


class MoleculeType(models.Model):
    molecule_type_name = models.TextField(blank=True, null=True)
    molecule_type_text = models.TextField(blank=True, null=True)
    molecule_type_id = models.AutoField(primary_key=True)
    molecule_type_secret = models.IntegerField(blank=True, null=True)
    molecule_type_created_by = models.TextField(blank=True, null=True)
    molecule_type_created_when = models.DateTimeField(blank=True, null=True)
    molecule_type_created_hashver = models.IntegerField(blank=True, null=True)
    molecule_type_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    molecule_type_changed_by = models.TextField(blank=True, null=True)
    molecule_type_changed_when = models.DateTimeField(blank=True, null=True)
    molecule_type_changed_hashver = models.IntegerField(blank=True, null=True)
    molecule_type_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'molecule_type'


class MpiOrder(models.Model):
    other_db_id = models.IntegerField(blank=True, null=True)
    order_person = models.TextField(blank=True, null=True)
    order_account = models.TextField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    molecule_name = models.TextField(blank=True, null=True)
    cas_nr = models.TextField(blank=True, null=True)
    chemical_storage_conc = models.FloatField(blank=True, null=True)
    chemical_storage_conc_unit = models.TextField(blank=True, null=True)
    chemical_storage_solvent = models.TextField(blank=True, null=True)
    supplier = models.TextField(blank=True, null=True)
    sap_bestell_nr = models.TextField(blank=True, null=True)
    sap_stamm_nr = models.TextField(blank=True, null=True)
    bessi = models.TextField(blank=True, null=True)
    mpi_order_status = models.CharField(max_length=9, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    amount_unit = models.TextField(blank=True, null=True)
    pos_liste = models.IntegerField(blank=True, null=True)
    mpi_order_id = models.AutoField(primary_key=True)
    mpi_order_secret = models.IntegerField(blank=True, null=True)
    mpi_order_created_by = models.TextField(blank=True, null=True)
    mpi_order_created_when = models.DateTimeField(blank=True, null=True)
    mpi_order_created_hashver = models.IntegerField(blank=True, null=True)
    mpi_order_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    mpi_order_changed_by = models.TextField(blank=True, null=True)
    mpi_order_changed_when = models.DateTimeField(blank=True, null=True)
    mpi_order_changed_hashver = models.IntegerField(blank=True, null=True)
    mpi_order_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpi_order'


class MpiOrderItem(models.Model):
    mpi_order_id = models.IntegerField(blank=True, null=True)
    chemical_storage_barcode = models.TextField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    amount_unit = models.TextField(blank=True, null=True)
    order_status = models.CharField(max_length=7, blank=True, null=True)
    mpi_order_item_id = models.AutoField(primary_key=True)
    mpi_order_item_secret = models.IntegerField(blank=True, null=True)
    mpi_order_item_created_by = models.TextField(blank=True, null=True)
    mpi_order_item_created_when = models.DateTimeField(blank=True, null=True)
    mpi_order_item_created_hashver = models.IntegerField(blank=True, null=True)
    mpi_order_item_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    mpi_order_item_changed_by = models.TextField(blank=True, null=True)
    mpi_order_item_changed_when = models.DateTimeField(blank=True, null=True)
    mpi_order_item_changed_hashver = models.IntegerField(blank=True, null=True)
    mpi_order_item_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpi_order_item'


class OrderAlternative(models.Model):
    chemical_order_id = models.IntegerField(blank=True, null=True)
    supplier = models.TextField(blank=True, null=True)
    catno = models.TextField(db_column='catNo', blank=True, null=True)  # Field name made lowercase.
    beautifulcatno = models.TextField(db_column='beautifulCatNo', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    cas_nr = models.TextField(blank=True, null=True)
    package_amount = models.FloatField(blank=True, null=True)
    package_amount_unit = models.TextField(blank=True, null=True)
    number_packages_text = models.TextField(blank=True, null=True)
    density_20 = models.FloatField(blank=True, null=True)
    number_packages = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    price_currency = models.TextField(blank=True, null=True)
    vat_rate = models.FloatField(blank=True, null=True)
    order_alternative_id = models.AutoField(primary_key=True)
    order_alternative_secret = models.IntegerField(blank=True, null=True)
    order_alternative_created_by = models.TextField(blank=True, null=True)
    order_alternative_created_when = models.DateTimeField(blank=True, null=True)
    order_alternative_created_hashver = models.IntegerField(blank=True, null=True)
    order_alternative_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    order_alternative_changed_by = models.TextField(blank=True, null=True)
    order_alternative_changed_when = models.DateTimeField(blank=True, null=True)
    order_alternative_changed_hashver = models.IntegerField(blank=True, null=True)
    order_alternative_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_alternative'


class OrderComp(models.Model):
    institution_id = models.IntegerField(blank=True, null=True)
    comp_order_date = models.DateField(blank=True, null=True)
    fixed_costs = models.FloatField(blank=True, null=True)
    fixed_costs_vat_rate = models.FloatField(blank=True, null=True)
    lagerpauschale = models.FloatField(blank=True, null=True)
    order_comp_status = models.CharField(max_length=16, blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    order_way = models.TextField(blank=True, null=True)
    order_identifier = models.TextField(blank=True, null=True)
    kleinauftrag_nrn = models.TextField(blank=True, null=True)
    central_cost_centre = models.TextField(blank=True, null=True)
    order_comp_id = models.AutoField(primary_key=True)
    order_comp_created_by = models.TextField(blank=True, null=True)
    order_comp_created_when = models.DateTimeField(blank=True, null=True)
    order_comp_created_hashver = models.IntegerField(blank=True, null=True)
    order_comp_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    order_comp_changed_by = models.TextField(blank=True, null=True)
    order_comp_changed_when = models.DateTimeField(blank=True, null=True)
    order_comp_changed_hashver = models.IntegerField(blank=True, null=True)
    order_comp_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_comp'


class OtherDb(models.Model):
    host = models.TextField(blank=True, null=True)
    db_name = models.TextField(blank=True, null=True)
    db_user = models.TextField(blank=True, null=True)
    db_pass = models.TextField(blank=True, null=True)
    db_beauty_name = models.TextField(blank=True, null=True)
    capabilities = models.CharField(max_length=17, blank=True, null=True)
    priority = models.SmallIntegerField(blank=True, null=True)
    other_db_id = models.AutoField(primary_key=True)
    other_db_secret = models.IntegerField(blank=True, null=True)
    other_db_disabled = models.IntegerField(blank=True, null=True)
    other_db_created_by = models.TextField(blank=True, null=True)
    other_db_created_when = models.DateTimeField(blank=True, null=True)
    other_db_created_hashver = models.IntegerField(blank=True, null=True)
    other_db_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    other_db_changed_by = models.TextField(blank=True, null=True)
    other_db_changed_when = models.DateTimeField(blank=True, null=True)
    other_db_changed_hashver = models.IntegerField(blank=True, null=True)
    other_db_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_db'


class PredefinedPermissions(models.Model):
    permission_level_name = models.TextField(blank=True, null=True)
    permissions = models.IntegerField(blank=True, null=True)
    predefined_permissions_id = models.AutoField(primary_key=True)
    predefined_permissions_created_by = models.TextField(blank=True, null=True)
    predefined_permissions_created_when = models.DateTimeField(blank=True, null=True)
    predefined_permissions_created_hashver = models.IntegerField(blank=True, null=True)
    predefined_permissions_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    predefined_permissions_changed_by = models.TextField(blank=True, null=True)
    predefined_permissions_changed_when = models.DateTimeField(blank=True, null=True)
    predefined_permissions_changed_hashver = models.IntegerField(blank=True, null=True)
    predefined_permissions_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'predefined_permissions'


class Project(models.Model):
    project_name = models.TextField(blank=True, null=True)
    project_text = models.TextField(blank=True, null=True)
    project_created_by = models.TextField(blank=True, null=True)
    project_created_when = models.DateField(blank=True, null=True)
    project_status = models.CharField(max_length=11, blank=True, null=True)
    project_members_only = models.IntegerField(blank=True, null=True)
    project_id = models.AutoField(primary_key=True)
    project_shared = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectLiterature(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    literature_id = models.IntegerField(blank=True, null=True)
    nr_in_project = models.IntegerField(blank=True, null=True)
    project_literature_id = models.AutoField(primary_key=True)
    project_literature_shared = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_literature'


class ProjectPerson(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    person_id = models.IntegerField(blank=True, null=True)
    project_person_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'project_person'


class Reaction(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True)
    reaction_type_id = models.IntegerField(blank=True, null=True)
    reaction_prototype = models.IntegerField(blank=True, null=True)
    reaction_prototype_db_id = models.IntegerField(blank=True, null=True)
    lab_journal = models.ForeignKey(LabJournal, blank=True, null=True)
    nr_in_lab_journal = models.SmallIntegerField(blank=True, null=True)
    realization_text = models.TextField(blank=True, null=True)
    realization_text_fulltext = models.TextField(blank=True, null=True)
    realization_observation = models.TextField(blank=True, null=True)
    realization_observation_fulltext = models.TextField(blank=True, null=True)
    rxn_smiles = models.TextField(blank=True, null=True)
    rxnfile_blob = models.BinaryField(blank=True, null=True)
    rxn_gif_file = models.BinaryField(blank=True, null=True)
    rxn_svg_file = models.BinaryField(blank=True, null=True)
    reaction_carried_out_by = models.TextField(blank=True, null=True)
    reaction_title = models.TextField(blank=True, null=True)
    reaction_quality = models.FloatField(blank=True, null=True)
    reaction_started_when = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    ref_amount = models.FloatField(blank=True, null=True)
    ref_amount_unit = models.TextField(blank=True, null=True)
    reaction_uid = models.CharField(max_length=128, blank=True, null=True)
    reaction_ext_archive_id = models.TextField(blank=True, null=True)
    reaction_id = models.AutoField(primary_key=True)
    reaction_shared = models.IntegerField(blank=True, null=True)
    reaction_disabled = models.IntegerField(blank=True, null=True)
    reaction_created_by = models.TextField(blank=True, null=True)
    reaction_created_when = models.DateTimeField(blank=True, null=True)
    reaction_created_hashver = models.IntegerField(blank=True, null=True)
    reaction_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    reaction_changed_by = models.TextField(blank=True, null=True)
    reaction_changed_when = models.DateTimeField(blank=True, null=True)
    reaction_changed_hashver = models.IntegerField(blank=True, null=True)
    reaction_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reaction'
        unique_together = (('lab_journal', 'nr_in_lab_journal'),)


class ReactionArchive(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    reaction_type_id = models.IntegerField(blank=True, null=True)
    reaction_prototype = models.IntegerField(blank=True, null=True)
    reaction_prototype_db_id = models.IntegerField(blank=True, null=True)
    lab_journal_id = models.IntegerField(blank=True, null=True)
    nr_in_lab_journal = models.SmallIntegerField(blank=True, null=True)
    realization_text = models.TextField(blank=True, null=True)
    realization_text_fulltext = models.TextField(blank=True, null=True)
    realization_observation = models.TextField(blank=True, null=True)
    realization_observation_fulltext = models.TextField(blank=True, null=True)
    rxn_smiles = models.TextField(blank=True, null=True)
    rxnfile_blob = models.TextField(blank=True, null=True)
    rxn_gif_file = models.TextField(blank=True, null=True)
    rxn_svg_file = models.TextField(blank=True, null=True)
    reaction_carried_out_by = models.TextField(blank=True, null=True)
    reaction_title = models.TextField(blank=True, null=True)
    reaction_quality = models.FloatField(blank=True, null=True)
    reaction_started_when = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    ref_amount = models.FloatField(blank=True, null=True)
    ref_amount_unit = models.TextField(blank=True, null=True)
    reaction_id = models.IntegerField(blank=True, null=True)
    reaction_shared = models.IntegerField(blank=True, null=True)
    reaction_disabled = models.IntegerField(blank=True, null=True)
    reaction_created_by = models.TextField(blank=True, null=True)
    reaction_created_when = models.DateTimeField(blank=True, null=True)
    reaction_created_hashver = models.IntegerField(blank=True, null=True)
    reaction_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    reaction_changed_by = models.TextField(blank=True, null=True)
    reaction_changed_when = models.DateTimeField(blank=True, null=True)
    reaction_changed_hashver = models.IntegerField(blank=True, null=True)
    reaction_changed_md5 = models.CharField(max_length=128, blank=True, null=True)
    archive_entity_id = models.IntegerField(blank=True, null=True)
    version_comment = models.TextField(blank=True, null=True)
    is_autosave = models.IntegerField(blank=True, null=True)
    reaction_archive_id = models.AutoField(primary_key=True)
    reaction_uid = models.CharField(max_length=128, blank=True, null=True)
    reaction_ext_archive_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reaction_archive'


class ReactionChemical(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True)
    reaction = models.ForeignKey(Reaction, blank=True, null=True)
    from_reaction_id = models.IntegerField(blank=True, null=True)
    from_reaction_chemical_id = models.IntegerField(blank=True, null=True)
    other_db = models.ForeignKey(OtherDb, blank=True, null=True)
    molecule = models.ForeignKey(Molecule, blank=True, null=True)
    chemical_storage = models.ForeignKey(ChemicalStorage, blank=True, null=True)
    chemical_storage_barcode = models.CharField(max_length=20, blank=True, null=True)
    mixture_with = models.IntegerField(blank=True, null=True)
    standard_name = models.TextField(blank=True, null=True)
    package_name = models.TextField(blank=True, null=True)
    cas_nr = models.TextField(blank=True, null=True)
    smiles = models.TextField(blank=True, null=True)
    smiles_stereo = models.TextField(blank=True, null=True)
    inchi = models.TextField(blank=True, null=True)
    molfile_blob = models.BinaryField(blank=True, null=True)
    molecule_serialized = models.BinaryField(blank=True, null=True)
    gif_file = models.BinaryField(blank=True, null=True)
    svg_file = models.BinaryField(blank=True, null=True)
    emp_formula = models.TextField(blank=True, null=True)
    mw = models.FloatField(blank=True, null=True)
    density_20 = models.FloatField(blank=True, null=True)
    rc_conc = models.FloatField(blank=True, null=True)
    rc_conc_unit = models.TextField(blank=True, null=True)
    safety_r = models.TextField(blank=True, null=True)
    safety_h = models.TextField(blank=True, null=True)
    safety_s = models.TextField(blank=True, null=True)
    safety_p = models.TextField(blank=True, null=True)
    safety_sym = models.TextField(blank=True, null=True)
    safety_sym_ghs = models.TextField(blank=True, null=True)
    nr_in_reaction = models.IntegerField(blank=True, null=True)
    addition_delay = models.TimeField(blank=True, null=True)
    addition_duration = models.TimeField(blank=True, null=True)
    role = models.CharField(max_length=12, blank=True, null=True)
    stoch_coeff = models.FloatField(blank=True, null=True)
    rc_purity = models.FloatField(blank=True, null=True)
    m_brutto = models.FloatField(blank=True, null=True)
    m_tara = models.FloatField(blank=True, null=True)
    mass_unit = models.TextField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    volume_unit = models.TextField(blank=True, null=True)
    rc_amount = models.FloatField(blank=True, null=True)
    rc_amount_unit = models.TextField(blank=True, null=True)
    gc_yield = models.FloatField(blank=True, null=True)
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)  # Field renamed because it was a Python
    # reserved word.
    measured = models.CharField(max_length=6, blank=True, null=True)
    colour = models.TextField(blank=True, null=True)
    consistency = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    reaction_chemical_id = models.AutoField(primary_key=True)
    fingerprint1 = models.IntegerField()
    fingerprint2 = models.IntegerField()
    fingerprint3 = models.IntegerField()
    fingerprint4 = models.IntegerField()
    fingerprint5 = models.IntegerField()
    fingerprint6 = models.IntegerField()
    fingerprint7 = models.IntegerField()
    fingerprint8 = models.IntegerField()
    fingerprint9 = models.IntegerField()
    fingerprint10 = models.IntegerField()
    fingerprint11 = models.IntegerField()
    fingerprint12 = models.IntegerField()
    fingerprint13 = models.IntegerField()
    fingerprint14 = models.IntegerField()
    fingerprint15 = models.IntegerField()
    fingerprint16 = models.IntegerField()
    reaction_chemical_shared = models.IntegerField(blank=True, null=True)
    reaction_chemical_created_by = models.TextField(blank=True, null=True)
    reaction_chemical_created_when = models.DateTimeField(blank=True, null=True)
    reaction_chemical_created_hashver = models.IntegerField(blank=True, null=True)
    reaction_chemical_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    reaction_chemical_changed_by = models.TextField(blank=True, null=True)
    reaction_chemical_changed_when = models.DateTimeField(blank=True, null=True)
    reaction_chemical_changed_hashver = models.IntegerField(blank=True, null=True)
    reaction_chemical_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reaction_chemical'


class ReactionChemicalArchive(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    reaction_id = models.IntegerField(blank=True, null=True)
    from_reaction_id = models.IntegerField(blank=True, null=True)
    from_reaction_chemical_id = models.IntegerField(blank=True, null=True)
    other_db_id = models.IntegerField(blank=True, null=True)
    molecule_id = models.IntegerField(blank=True, null=True)
    chemical_storage_id = models.IntegerField(blank=True, null=True)
    chemical_storage_barcode = models.CharField(max_length=20, blank=True, null=True)
    mixture_with = models.IntegerField(blank=True, null=True)
    standard_name = models.TextField(blank=True, null=True)
    package_name = models.TextField(blank=True, null=True)
    cas_nr = models.TextField(blank=True, null=True)
    smiles = models.TextField(blank=True, null=True)
    smiles_stereo = models.TextField(blank=True, null=True)
    inchi = models.TextField(blank=True, null=True)
    molfile_blob = models.TextField(blank=True, null=True)
    molecule_serialized = models.TextField(blank=True, null=True)
    gif_file = models.TextField(blank=True, null=True)
    svg_file = models.TextField(blank=True, null=True)
    emp_formula = models.TextField(blank=True, null=True)
    mw = models.FloatField(blank=True, null=True)
    density_20 = models.FloatField(blank=True, null=True)
    rc_conc = models.FloatField(blank=True, null=True)
    rc_conc_unit = models.TextField(blank=True, null=True)
    safety_r = models.TextField(blank=True, null=True)
    safety_h = models.TextField(blank=True, null=True)
    safety_s = models.TextField(blank=True, null=True)
    safety_p = models.TextField(blank=True, null=True)
    safety_sym = models.TextField(blank=True, null=True)
    safety_sym_ghs = models.TextField(blank=True, null=True)
    nr_in_reaction = models.IntegerField(blank=True, null=True)
    addition_delay = models.TimeField(blank=True, null=True)
    addition_duration = models.TimeField(blank=True, null=True)
    role = models.CharField(max_length=12, blank=True, null=True)
    stoch_coeff = models.FloatField(blank=True, null=True)
    rc_purity = models.FloatField(blank=True, null=True)
    m_brutto = models.FloatField(blank=True, null=True)
    m_tara = models.FloatField(blank=True, null=True)
    mass_unit = models.TextField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    volume_unit = models.TextField(blank=True, null=True)
    rc_amount = models.FloatField(blank=True, null=True)
    rc_amount_unit = models.TextField(blank=True, null=True)
    gc_yield = models.FloatField(blank=True, null=True)
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)  # Field renamed because it was a Python
    # reserved word.
    measured = models.CharField(max_length=6, blank=True, null=True)
    colour = models.TextField(blank=True, null=True)
    consistency = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    reaction_chemical_id = models.IntegerField(blank=True, null=True)
    fingerprint1 = models.IntegerField()
    fingerprint2 = models.IntegerField()
    fingerprint3 = models.IntegerField()
    fingerprint4 = models.IntegerField()
    fingerprint5 = models.IntegerField()
    fingerprint6 = models.IntegerField()
    fingerprint7 = models.IntegerField()
    fingerprint8 = models.IntegerField()
    fingerprint9 = models.IntegerField()
    fingerprint10 = models.IntegerField()
    fingerprint11 = models.IntegerField()
    fingerprint12 = models.IntegerField()
    fingerprint13 = models.IntegerField()
    fingerprint14 = models.IntegerField()
    fingerprint15 = models.IntegerField()
    fingerprint16 = models.IntegerField()
    reaction_chemical_shared = models.IntegerField(blank=True, null=True)
    reaction_chemical_created_by = models.TextField(blank=True, null=True)
    reaction_chemical_created_when = models.DateTimeField(blank=True, null=True)
    reaction_chemical_created_hashver = models.IntegerField(blank=True, null=True)
    reaction_chemical_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    reaction_chemical_changed_by = models.TextField(blank=True, null=True)
    reaction_chemical_changed_when = models.DateTimeField(blank=True, null=True)
    reaction_chemical_changed_hashver = models.IntegerField(blank=True, null=True)
    reaction_chemical_changed_md5 = models.CharField(max_length=128, blank=True, null=True)
    archive_entity_id = models.IntegerField(blank=True, null=True)
    version_comment = models.TextField(blank=True, null=True)
    is_autosave = models.IntegerField(blank=True, null=True)
    reaction_chemical_archive_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'reaction_chemical_archive'


class ReactionChemicalProperty(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    reaction_chemical_id = models.IntegerField(blank=True, null=True)
    reaction_chemical_property_name = models.TextField(blank=True, null=True)
    reaction_chemical_property_value = models.TextField(blank=True, null=True)
    reaction_chemical_property_number = models.FloatField(blank=True, null=True)
    reaction_chemical_property_id = models.AutoField(primary_key=True)
    reaction_chemical_property_shared = models.IntegerField(blank=True, null=True)
    reaction_chemical_property_created_by = models.TextField(blank=True, null=True)
    reaction_chemical_property_created_when = models.DateTimeField(blank=True, null=True)
    reaction_chemical_property_created_hashver = models.IntegerField(blank=True, null=True)
    reaction_chemical_property_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    reaction_chemical_property_changed_by = models.TextField(blank=True, null=True)
    reaction_chemical_property_changed_when = models.DateTimeField(blank=True, null=True)
    reaction_chemical_property_changed_hashver = models.IntegerField(blank=True, null=True)
    reaction_chemical_property_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reaction_chemical_property'


class ReactionChemicalPropertyArchive(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    reaction_chemical_id = models.IntegerField(blank=True, null=True)
    reaction_chemical_property_name = models.TextField(blank=True, null=True)
    reaction_chemical_property_value = models.TextField(blank=True, null=True)
    reaction_chemical_property_number = models.FloatField(blank=True, null=True)
    reaction_chemical_property_id = models.IntegerField(blank=True, null=True)
    reaction_chemical_property_shared = models.IntegerField(blank=True, null=True)
    reaction_chemical_property_created_by = models.TextField(blank=True, null=True)
    reaction_chemical_property_created_when = models.DateTimeField(blank=True, null=True)
    reaction_chemical_property_created_hashver = models.IntegerField(blank=True, null=True)
    reaction_chemical_property_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    reaction_chemical_property_changed_by = models.TextField(blank=True, null=True)
    reaction_chemical_property_changed_when = models.DateTimeField(blank=True, null=True)
    reaction_chemical_property_changed_hashver = models.IntegerField(blank=True, null=True)
    reaction_chemical_property_changed_md5 = models.CharField(max_length=128, blank=True, null=True)
    archive_entity_id = models.IntegerField(blank=True, null=True)
    version_comment = models.TextField(blank=True, null=True)
    is_autosave = models.IntegerField(blank=True, null=True)
    reaction_chemical_property_archive_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'reaction_chemical_property_archive'


class ReactionLiterature(models.Model):
    reaction_id = models.IntegerField(blank=True, null=True)
    literature_id = models.IntegerField(blank=True, null=True)
    reaction_literature_id = models.AutoField(primary_key=True)
    reaction_literature_secret = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reaction_literature'


class ReactionLiteratureArchive(models.Model):
    reaction_id = models.IntegerField(blank=True, null=True)
    literature_id = models.IntegerField(blank=True, null=True)
    reaction_literature_id = models.IntegerField(blank=True, null=True)
    reaction_literature_secret = models.IntegerField(blank=True, null=True)
    archive_entity_id = models.IntegerField(blank=True, null=True)
    version_comment = models.TextField(blank=True, null=True)
    is_autosave = models.IntegerField(blank=True, null=True)
    reaction_literature_archive_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'reaction_literature_archive'


class ReactionProperty(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    reaction_id = models.IntegerField(blank=True, null=True)
    reaction_property_name = models.TextField(blank=True, null=True)
    reaction_property_value = models.TextField(blank=True, null=True)
    reaction_property_number = models.FloatField(blank=True, null=True)
    reaction_property_unit = models.TextField(blank=True, null=True)
    reaction_property_id = models.AutoField(primary_key=True)
    reaction_property_shared = models.IntegerField(blank=True, null=True)
    reaction_property_created_by = models.TextField(blank=True, null=True)
    reaction_property_created_when = models.DateTimeField(blank=True, null=True)
    reaction_property_created_hashver = models.IntegerField(blank=True, null=True)
    reaction_property_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    reaction_property_changed_by = models.TextField(blank=True, null=True)
    reaction_property_changed_when = models.DateTimeField(blank=True, null=True)
    reaction_property_changed_hashver = models.IntegerField(blank=True, null=True)
    reaction_property_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reaction_property'


class ReactionPropertyArchive(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    reaction_id = models.IntegerField(blank=True, null=True)
    reaction_property_name = models.TextField(blank=True, null=True)
    reaction_property_value = models.TextField(blank=True, null=True)
    reaction_property_number = models.FloatField(blank=True, null=True)
    reaction_property_unit = models.TextField(blank=True, null=True)
    reaction_property_id = models.IntegerField(blank=True, null=True)
    reaction_property_shared = models.IntegerField(blank=True, null=True)
    reaction_property_created_by = models.TextField(blank=True, null=True)
    reaction_property_created_when = models.DateTimeField(blank=True, null=True)
    reaction_property_created_hashver = models.IntegerField(blank=True, null=True)
    reaction_property_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    reaction_property_changed_by = models.TextField(blank=True, null=True)
    reaction_property_changed_when = models.DateTimeField(blank=True, null=True)
    reaction_property_changed_hashver = models.IntegerField(blank=True, null=True)
    reaction_property_changed_md5 = models.CharField(max_length=128, blank=True, null=True)
    archive_entity_id = models.IntegerField(blank=True, null=True)
    version_comment = models.TextField(blank=True, null=True)
    is_autosave = models.IntegerField(blank=True, null=True)
    reaction_property_archive_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'reaction_property_archive'


class ReactionType(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    reaction_type_name = models.TextField(blank=True, null=True)
    reaction_type_text = models.TextField(blank=True, null=True)
    reaction_type_id = models.AutoField(primary_key=True)
    reaction_type_secret = models.IntegerField(blank=True, null=True)
    reaction_type_created_by = models.TextField(blank=True, null=True)
    reaction_type_created_when = models.DateTimeField(blank=True, null=True)
    reaction_type_created_hashver = models.IntegerField(blank=True, null=True)
    reaction_type_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    reaction_type_changed_by = models.TextField(blank=True, null=True)
    reaction_type_changed_when = models.DateTimeField(blank=True, null=True)
    reaction_type_changed_hashver = models.IntegerField(blank=True, null=True)
    reaction_type_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reaction_type'


class Rent(models.Model):
    item_identifier = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    order_cost_centre_cp = models.TextField(blank=True, null=True)
    order_acc_no_cp = models.TextField(blank=True, null=True)
    price_per_day = models.FloatField(blank=True, null=True)
    price_per_day_currency = models.TextField(blank=True, null=True)
    vat_rate = models.FloatField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    billing_date = models.DateField(blank=True, null=True)
    settlement_id = models.IntegerField(blank=True, null=True)
    rent_id = models.AutoField(primary_key=True)
    rent_secret = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rent'


class RetentionTime(models.Model):
    analytics_type_id = models.IntegerField(blank=True, null=True)
    analytics_device_id = models.IntegerField(blank=True, null=True)
    analytics_method_id = models.IntegerField(blank=True, null=True)
    molecule_id = models.IntegerField(blank=True, null=True)
    reaction_chemical_id = models.IntegerField(blank=True, null=True)
    smiles_stereo = models.TextField(blank=True, null=True)
    smiles = models.TextField(blank=True, null=True)
    retention_time = models.FloatField(blank=True, null=True)
    response_factor = models.FloatField(blank=True, null=True)
    retention_time_id = models.AutoField(primary_key=True)
    retention_time_created_by = models.TextField(blank=True, null=True)
    retention_time_created_when = models.DateTimeField(blank=True, null=True)
    retention_time_created_hashver = models.IntegerField(blank=True, null=True)
    retention_time_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    retention_time_changed_by = models.TextField(blank=True, null=True)
    retention_time_changed_when = models.DateTimeField(blank=True, null=True)
    retention_time_changed_hashver = models.IntegerField(blank=True, null=True)
    retention_time_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'retention_time'
        unique_together = (('analytics_type_id', 'analytics_device_id', 'analytics_method_id', 'molecule_id'),)


class SciJournal(models.Model):
    sci_journal_name = models.TextField(blank=True, null=True)
    sci_journal_abbrev = models.TextField(blank=True, null=True)
    sci_journal_impact_factor = models.FloatField(blank=True, null=True)
    sci_journal_publisher = models.TextField(blank=True, null=True)
    sci_journal_driver = models.TextField(blank=True, null=True)
    sci_journal_id = models.AutoField(primary_key=True)
    sci_journal_secret = models.IntegerField(blank=True, null=True)
    sci_journal_created_by = models.TextField(blank=True, null=True)
    sci_journal_created_when = models.DateTimeField(blank=True, null=True)
    sci_journal_created_hashver = models.IntegerField(blank=True, null=True)
    sci_journal_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    sci_journal_changed_by = models.TextField(blank=True, null=True)
    sci_journal_changed_when = models.DateTimeField(blank=True, null=True)
    sci_journal_changed_hashver = models.IntegerField(blank=True, null=True)
    sci_journal_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sci_journal'


class Settlement(models.Model):
    billing_date = models.DateField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    lagerpauschale = models.FloatField(blank=True, null=True)
    settlement_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'settlement'


class Storage(models.Model):
    storage_name = models.TextField(blank=True, null=True)
    institution_id = models.IntegerField(blank=True, null=True)
    poison_cabinet = models.IntegerField(blank=True, null=True)
    storage_id = models.AutoField(primary_key=True)
    storage_created_by = models.TextField(blank=True, null=True)
    storage_created_when = models.DateTimeField(blank=True, null=True)
    storage_created_hashver = models.IntegerField(blank=True, null=True)
    storage_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    storage_changed_by = models.TextField(blank=True, null=True)
    storage_changed_when = models.DateTimeField(blank=True, null=True)
    storage_changed_hashver = models.IntegerField(blank=True, null=True)
    storage_changed_md5 = models.CharField(max_length=128, blank=True, null=True)
    storage_barcode = models.CharField(max_length=20, blank=True, null=True)
    storage_secret = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage'


class SupplierOffer(models.Model):
    molecule_id = models.IntegerField(blank=True, null=True)
    supplier = models.TextField(blank=True, null=True)
    catno = models.TextField(db_column='catNo', blank=True, null=True)  # Field name made lowercase.
    beautifulcatno = models.TextField(db_column='beautifulCatNo', blank=True, null=True)  # Field name made lowercase.
    so_purity = models.TextField(blank=True, null=True)
    so_package_amount = models.FloatField(blank=True, null=True)
    so_package_amount_unit = models.TextField(blank=True, null=True)
    so_price = models.FloatField(blank=True, null=True)
    so_price_currency = models.TextField(blank=True, null=True)
    so_vat_rate = models.FloatField(blank=True, null=True)
    so_date = models.DateTimeField(blank=True, null=True)
    comment_supplier_offer = models.TextField(blank=True, null=True)
    supplier_offer_id = models.AutoField(primary_key=True)
    supplier_offer_secret = models.IntegerField(blank=True, null=True)
    supplier_offer_created_by = models.TextField(blank=True, null=True)
    supplier_offer_created_when = models.DateTimeField(blank=True, null=True)
    supplier_offer_created_hashver = models.IntegerField(blank=True, null=True)
    supplier_offer_created_md5 = models.CharField(max_length=128, blank=True, null=True)
    supplier_offer_changed_by = models.TextField(blank=True, null=True)
    supplier_offer_changed_when = models.DateTimeField(blank=True, null=True)
    supplier_offer_changed_hashver = models.IntegerField(blank=True, null=True)
    supplier_offer_changed_md5 = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_offer'


class Units(models.Model):
    unit_name = models.TextField(blank=True, null=True)
    unit_factor = models.FloatField(blank=True, null=True)
    unit_type = models.TextField(blank=True, null=True)
    unit_is_standard = models.IntegerField(blank=True, null=True)
    units_id = models.AutoField(primary_key=True)
    units_disabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'units'


class XyData(models.Model):
    analytical_data_id = models.IntegerField(blank=True, null=True)
    retention_time = models.FloatField(blank=True, null=True)
    val_x = models.FloatField(blank=True, null=True)
    val_y = models.FloatField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    xy_data_id = models.AutoField(primary_key=True)
    xy_data_shared = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xy_data'


class XyDataArchive(models.Model):
    analytical_data_id = models.IntegerField(blank=True, null=True)
    retention_time = models.FloatField(blank=True, null=True)
    val_x = models.FloatField(blank=True, null=True)
    val_y = models.FloatField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    xy_data_id = models.IntegerField(blank=True, null=True)
    xy_data_shared = models.IntegerField(blank=True, null=True)
    archive_entity_id = models.IntegerField(blank=True, null=True)
    version_comment = models.TextField(blank=True, null=True)
    is_autosave = models.IntegerField(blank=True, null=True)
    xy_data_archive_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'xy_data_archive'
