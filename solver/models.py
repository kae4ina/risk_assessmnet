from django.db import models
from django.db.models import ForeignKey, CASCADE, FloatField, CharField, Min

from assets.models import DefaultAssetCategory


class DefaultVulnerability(models.Model):
    name = models.CharField(max_length=150)

    def __self__(self):
        return self.name


class ThreatType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class DefaultThreat(models.Model):
    id = models.CharField(max_length=150, primary_key=True)

    name = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=1500, null=True, blank=True)
    source = models.CharField(max_length=500, null=True)
    destination = models.CharField(max_length=500, null=True)

    destruction_of_confidence = models.BooleanField(null=True)
    destruction_of_integrity = models.BooleanField(null=True)
    destruction_of_availability = models.BooleanField(null=True)
    def __str__(self):
        return self.name

class DefaultMeasureGroup(models.Model):
    id = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class DefaultMeasureSubgroup(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    group = ForeignKey(to=DefaultMeasureGroup, on_delete=CASCADE, default=1, null=True)
    name = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name

class DefaultMeasure(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=500)
    subgroup = ForeignKey(to=DefaultMeasureSubgroup, on_delete=CASCADE, default=1)
    koef=models.FloatField(default=0.5)
    #related_threat = ForeignKey(to=DefaultThreat, on_delete=CASCADE, default=1)  # парируемая угроза
    def __str__(self):
        return self.name




class GeneralThreats(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=700)
    possibility_of_occurrence=models.FloatField(default=0.5)
    possibility_of_success=models.FloatField(default=0.5)

    def __str__(self):
        return self.name

class GroupWays(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name=models.CharField(max_length=200)

class Ways(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name=models.CharField(max_length=200)
    group = ForeignKey(to=GroupWays, on_delete=CASCADE)
    def __str__(self):
        return self.name

class ThreatWays(models.Model):
    generalthreat=ForeignKey(to=GeneralThreats, on_delete=CASCADE)
    way=ForeignKey(to=Ways, on_delete=CASCADE)


class GeneralObjects(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=700)
    def __str__(self):
        return self.name

class ThreatObject(models.Model):
      id_object=ForeignKey(to=GeneralObjects, on_delete=CASCADE)
      id_generalthreat=ForeignKey(to=GeneralThreats,on_delete=CASCADE)


class UserRisk(models.Model):
    name=CharField(max_length=150)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    general_object = models.ForeignKey(GeneralObjects, on_delete=models.CASCADE)
    threats = models.ManyToManyField(GeneralThreats)
    ways = models.ManyToManyField(Ways)
    created_at = models.DateTimeField(auto_now_add=True)
    money_loss=FloatField()
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.general_object.name}"

    @property
    def risk_score(self):
        """
        Степень риска:
        Σ (possibility_of_occurrence * 100 * possibility_of_success) * money_loss
        где сумма берется по всем связанным угрозам
        """
        total_risk = 0
        for threat in self.threats.all():
            threat_risk = (threat.possibility_of_occurrence * 100 *
                           threat.possibility_of_success)
            total_risk += threat_risk

        return total_risk * self.money_loss

    @property
    def current_risk_score(self):

        completed_measures = DefaultMeasure.objects.filter(
            tasks__risk_relations__risk=self,
            tasks__status_id=1
        )

        if not completed_measures.exists():
            return self.risk_score

        min_koef = completed_measures.aggregate(min=Min('koef'))['min']
        return self.mitigated_risk_score(min_koef)

    def mitigated_risk_score(self, measure_koef):
        """
        Степень риска после применения меры с коэффициентом measure_koef
        Σ (|threat.possibility_of_occurrence - measure_koef| * 100 * possibility_of_success) * money_loss
        """
        total_risk = 0
        for threat in self.threats.all():
            adjusted_possibility = abs(threat.possibility_of_occurrence - measure_koef)
            threat_risk = (adjusted_possibility * 100 * threat.possibility_of_success)
            total_risk += threat_risk

        return total_risk * self.money_loss

    def get_risk_level(self):

        score = self.current_risk_score
        if score < 500000:
            level = "Низкий"
        elif 500000 <= score < 10000000:
            level = "Средний"
        else:
            level = "Высокий"

        return {
            'value': score,
            'text': level,
            'class': 'low' if score < 500000 else 'medium' if score < 10000000 else 'high'
        }

class RulesThreat(models.Model):
        measure = ForeignKey(to=DefaultMeasure, on_delete=CASCADE)
        threat = ForeignKey(to=GeneralThreats, on_delete=CASCADE, default=1)
        num = CharField(max_length=4)

        def __str__(self):
            measure_name = self.measure.name if hasattr(self.measure, 'name') else "Мера не указана"
            threat_name = self.threat.name if hasattr(self.threat, 'name') else "Угроза не указана"

            return f" Мера — {measure_name}"
            #return f"Правило: Мера — {measure_name}, Угроза — {threat_name}"

