# Generated by Django 3.2.6 on 2023-02-26 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ActiveDeliverySalesRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesId', models.FloatField(default=0)),
                ('deliveryCustName', models.CharField(max_length=100)),
                ('deliveryProductData', models.JSONField()),
                ('productValue', models.FloatField()),
                ('modeOfPayment', models.CharField(max_length=100)),
                ('amtFromCustomer', models.FloatField(default=0)),
                ('customerDebt', models.FloatField(default=0)),
                ('customerCredit', models.FloatField(default=0)),
                ('purchasedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('referenceName', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('company', models.CharField(max_length=100, null=True)),
                ('costPrice', models.FloatField()),
                ('subPrice', models.FloatField()),
                ('wholesalePrice', models.FloatField()),
                ('retailPrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ClosingStockHistory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('productsData', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('referenceName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('message_type', models.CharField(max_length=100)),
                ('message_content', models.CharField(max_length=1000)),
                ('message_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewStockHistory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('productsData', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='OpeningStockHistory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('productsData', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('referenceName', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('costPrice', models.FloatField()),
                ('subPrice', models.FloatField()),
                ('wholesalePrice', models.FloatField()),
                ('retailPrice', models.FloatField()),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='audit.company')),
            ],
        ),
        migrations.CreateModel(
            name='Remmittance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopSalesHandover', models.FloatField(default=0)),
                ('shopDeliveryHandover', models.FloatField(default=0)),
                ('remmittedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShopDeliveryRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('driverName', models.CharField(max_length=100)),
                ('deliveryNumber', models.FloatField(default=0)),
                ('productData', models.JSONField(default=dict)),
                ('amountBroughtBack', models.FloatField(blank=True, default=0)),
                ('deliveryStatus', models.CharField(default='delivering', max_length=100)),
                ('leftAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubDistributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TodayAudit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('totalAuditId', models.FloatField(default=0.0)),
                ('driver', models.CharField(default='Driver Name not set', max_length=100)),
                ('shopAttendant', models.CharField(default='Shop Attendant name not Set', max_length=100)),
                ('driverStatus', models.CharField(default='Driver has not closed', max_length=100)),
                ('shopAttendantStatus', models.CharField(default='Shop attendant has not closed', max_length=100)),
                ('openingStock', models.JSONField(default=dict)),
                ('newStock', models.JSONField(default=dict)),
                ('closingStock', models.JSONField(default=dict)),
                ('driverDeliveryStockDetails', models.JSONField(default=dict)),
                ('shopAttendantDeliveryStockDetails', models.JSONField(default=dict)),
                ('expectedDriverDeliveryStockDetails', models.JSONField(default=dict)),
                ('expectedShopAttendantDeliveryStockDetails', models.JSONField(default=dict)),
                ('deliveryCustomersToTransfer', models.JSONField(default=dict)),
                ('invoiceNumbers', models.JSONField(default=dict)),
                ('allSubSales', models.JSONField(default=dict)),
                ('allWholesales', models.JSONField(default=dict)),
                ('allRetailSales', models.JSONField(default=dict)),
                ('shopCustomersToTransfer', models.JSONField(default=dict)),
                ('shopHandover', models.FloatField(default=0)),
                ('TotalDeliveryHandover', models.FloatField(default=0)),
                ('fullShopSalesAudit', models.JSONField(default=dict)),
                ('fullDeliverySalesAudit', models.JSONField(default=dict)),
                ('customersInDebt', models.JSONField(default=dict)),
                ('customersCredit', models.JSONField(default=dict)),
                ('messages', models.JSONField(default=dict)),
                ('auditDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodayDeliverySalesRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliveryNumber', models.IntegerField(default=0)),
                ('salesId', models.FloatField(default=0)),
                ('allCustomerData', models.JSONField()),
                ('finishedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodayDeliveryStartRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('deliveryNumber', models.IntegerField(default=0)),
                ('salesId', models.FloatField(default=0)),
                ('productsData', models.JSONField(default=dict)),
                ('amountBroughtBack', models.FloatField(blank=True, default=0)),
                ('finishedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodayInvoiceNumber',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('invoiceNumber', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='todayTauditId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditId', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TotalAudit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('totalAuditId', models.FloatField(default=0.0)),
                ('driver', models.CharField(default='Driver Name not set', max_length=100)),
                ('shopAttendant', models.CharField(default='Shop Attendant name not Set', max_length=100)),
                ('driverStatus', models.CharField(default='Driver has not closed', max_length=100)),
                ('shopAttendantStatus', models.CharField(default='Shop attendant has not closed', max_length=100)),
                ('openingStock', models.JSONField(default=dict)),
                ('newStock', models.JSONField(default=dict)),
                ('closingStock', models.JSONField(default=dict)),
                ('driverDeliveryStockDetails', models.JSONField(default=dict)),
                ('shopAttendantDeliveryStockDetails', models.JSONField(default=dict)),
                ('expectedDriverDeliveryStockDetails', models.JSONField(default=dict)),
                ('expectedShopAttendantDeliveryStockDetails', models.JSONField(default=dict)),
                ('deliveryCustomersToTransfer', models.JSONField(default=dict)),
                ('invoiceNumbers', models.JSONField(default=dict)),
                ('allSubSales', models.JSONField(default=dict)),
                ('allWholesales', models.JSONField(default=dict)),
                ('allRetailSales', models.JSONField(default=dict)),
                ('shopCustomersToTransfer', models.JSONField(default=dict)),
                ('shopHandover', models.FloatField(default=0)),
                ('TotalDeliveryHandover', models.FloatField(default=0)),
                ('fullShopSalesAudit', models.JSONField(default=dict)),
                ('fullDeliverySalesAudit', models.JSONField(default=dict)),
                ('customersInDebt', models.JSONField(default=dict)),
                ('customersCredit', models.JSONField(default=dict)),
                ('messages', models.JSONField(default=dict)),
                ('auditDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WholesaleRecord',
            fields=[
                ('customerId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('customerName', models.CharField(max_length=100)),
                ('productsData', models.JSONField(default=dict)),
                ('productValue', models.FloatField(default=0)),
                ('modeOfPayment', models.CharField(default='Cash', max_length=100)),
                ('amtFromCustomer', models.FloatField(default=0)),
                ('customerDebt', models.FloatField(default=0)),
                ('customerCredit', models.FloatField(default=0)),
                ('soldAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodayOpeningStock',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('addedAt', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='audit.products')),
            ],
        ),
        migrations.CreateModel(
            name='TodayNewStock',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('addedAt', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='audit.products')),
            ],
        ),
        migrations.CreateModel(
            name='TodayClosingStock',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('addedAt', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='audit.products')),
            ],
        ),
        migrations.CreateModel(
            name='SubRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('productData', models.JSONField(default=dict)),
                ('productValue', models.FloatField(default=0)),
                ('modeOfPayment', models.CharField(default='Cash', max_length=100)),
                ('amtFromSubDistributor', models.FloatField(default=0)),
                ('subDistributorDebt', models.FloatField(default=0)),
                ('subDistributorCredit', models.FloatField(default=0)),
                ('soldAt', models.DateTimeField(auto_now_add=True)),
                ('subName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.subdistributors')),
            ],
        ),
        migrations.CreateModel(
            name='RetailRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('productQuantity', models.IntegerField()),
                ('productPrice', models.IntegerField(blank=True, null=True)),
                ('soldAt', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.products')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('accessStat', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('invoiceNumber', models.CharField(max_length=100)),
                ('invoiceImage', models.ImageField(upload_to='')),
                ('addedAt', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='audit.company')),
            ],
        ),
        migrations.CreateModel(
            name='ActiveDeliveryStartRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('salesId', models.FloatField(default=0)),
                ('productTakenQuantity', models.IntegerField()),
                ('productQuantityBroughtBack', models.IntegerField(blank=True, default=0)),
                ('amountBroughtBack', models.FloatField(blank=True, default=0)),
                ('leftAt', models.DateTimeField(auto_now_add=True)),
                ('productTaken', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.products')),
            ],
        ),
    ]
