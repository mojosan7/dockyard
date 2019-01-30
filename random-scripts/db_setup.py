from computecalc.models import Computecalc
c1 = Computecalc(aws_sku="1", aws_vCPU="1", aws_ram="2", aws_cost_per_hour="0.023", do_sku_equivalent="$5 droplet", do_cost_per_month="5")
c1.save()

c2 = Computecalc(aws_sku="t2.medium", aws_vCPU="2", aws_ram="4", aws_cost_per_hour="0.0464", do_sku_equivalent="$10 droplet", do_cost_per_month="10")
c2.save()

c3 = Computecalc(aws_sku="t2.xlarge", aws_vCPU="4", aws_ram="8", aws_cost_per_hour="0.1856", do_sku_equivalent="$20 droplet", do_cost_per_month="20")
c3.save()

c4 = Computecalc(aws_sku="t2.micro", aws_vCPU="8", aws_ram="16", aws_cost_per_hour=".0116", do_sku_equivalent="$40 droplet", do_cost_per_month="40")
c4.save()

c5 = Computecalc(aws_sku="t2.2xlarge", aws_vCPU="1", aws_ram="2", aws_cost_per_hour="0.3712", do_sku_equivalent="$5 droplet", do_cost_per_month="5")
c5.save()

c6 = Computecalc(aws_sku="t1.micro", aws_vCPU="2", aws_ram="4", aws_cost_per_hour="0..02", do_sku_equivalent="$10 droplet", do_cost_per_month="10")
c6.save()

c7 = Computecalc(aws_sku="m4.large", aws_vCPU="4", aws_ram="8", aws_cost_per_hour="0.1", do_sku_equivalent="$20 droplet", do_cost_per_month="20")
c7.save()

c8 = Computecalc(aws_sku="m4.xlarge", aws_vCPU="4", aws_ram="8", aws_cost_per_hour="0.2", do_sku_equivalent="$20 droplet", do_cost_per_month="20")
c8.save()

c9 = Computecalc(aws_sku="m4.2xlarge", aws_vCPU="8", aws_ram="16", aws_cost_per_hour="0.4", do_sku_equivalent="$40 droplet", do_cost_per_month="40")
c9.save()

c10 = Computecalc(aws_sku="m3.xlarge", aws_vCPU="1", aws_ram="2", aws_cost_per_hour="0.266", do_sku_equivalent="$5 droplet", do_cost_per_month="5")
c10.save()

c11 = Computecalc(aws_sku="m3.medium", aws_vCPU="2", aws_ram="4", aws_cost_per_hour="0.067", do_sku_equivalent="$10 droplet", do_cost_per_month="10")
c11.save()

c12 = Computecalc(aws_sku="m3.large", aws_vCPU="4", aws_ram="8", aws_cost_per_hour="0.133", do_sku_equivalent="$20 droplet", do_cost_per_month="20")
c12.save()

c13 = Computecalc(aws_sku="m3.2xlarge", aws_vCPU="8", aws_ram="16", aws_cost_per_hour="0.532", do_sku_equivalent="$40 droplet", do_cost_per_month="40")
c13.save()

c14 = Computecalc(aws_sku="m1.small", aws_vCPU="1", aws_ram="2", aws_cost_per_hour="0.044", do_sku_equivalent="$5 droplet", do_cost_per_month="5")
c14.save()

c15 = Computecalc(aws_sku="m1.medium", aws_vCPU="2", aws_ram="4", aws_cost_per_hour="0.087", do_sku_equivalent="$10 droplet", do_cost_per_month="10")
c15.save()

c16 = Computecalc(aws_sku="m1.large", aws_vCPU="4", aws_ram="8", aws_cost_per_hour="0.175", do_sku_equivalent="$20 droplet", do_cost_per_month="20")
c16.save()

c17 = Computecalc(aws_sku="c4.xlarge", aws_vCPU="8", aws_ram="16", aws_cost_per_hour="1.4", do_sku_equivalent="$40 droplet", do_cost_per_month="40")
c17.save()

c18 = Computecalc(aws_sku="c4.2xlarge", aws_vCPU="1", aws_ram="2", aws_cost_per_hour="0.023", do_sku_equivalent="$5 droplet", do_cost_per_month="5")
c18.save()

c19 = Computecalc(aws_sku="c3.large", aws_vCPU="4", aws_ram="8", aws_cost_per_hour="0.9", do_sku_equivalent="$20 droplet", do_cost_per_month="20")
c19.save()

c20 = Computecalc(aws_sku="c3.2xlarge", aws_vCPU="8", aws_ram="16", aws_cost_per_hour="1.4", do_sku_equivalent="$40 droplet", do_cost_per_month="40")
c20.save()

c21 = Computecalc(aws_sku="c4.4xlarge", aws_vCPU="1", aws_ram="2", aws_cost_per_hour="0.023", do_sku_equivalent="$5 droplet", do_cost_per_month="5")
c21.save()

c22 = Computecalc(aws_sku="c5.2xlarge", aws_vCPU="2", aws_ram="4", aws_cost_per_hour="0.6666", do_sku_equivalent="$10 droplet", do_cost_per_month="10")
c22.save()

c23 = Computecalc(aws_sku="c5.4xlarge", aws_vCPU="4", aws_ram="8", aws_cost_per_hour="0.9", do_sku_equivalent="$20 droplet", do_cost_per_month="20")
c23.save()
