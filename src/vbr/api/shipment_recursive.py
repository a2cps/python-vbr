from typing import List

from vbr.tableclasses import Biosample, Measurement, Shipment
from vbr.tableclasses.single_tables import Subject

from .biosample import BiosampleApi
from .container_logistics import ContainerLogisticsApi
from .measurement_logistics import MeasurementLogisticsApi
from .subject import SubjectApi


class RecursiveShipmentApi(object):
    def measurements_in_shipment(self, shipment: Shipment) -> List[Measurement]:
        """Returns a list of Measurements in a Shipment."""
        # Top level shipping containers. Probably just the virtual shipping box but
        # just in case not, include in the list of containers we pull measurements for
        containers = ContainerLogisticsApi.get_containers_for_shipment(self, shipment)
        child_containers = []
        for tc in containers:
            resp = ContainerLogisticsApi.get_container_children(self, tc)
            child_containers.extend(resp)
        child_containers = list(set(child_containers))
        containers.extend(child_containers)
        measurements = []
        for cont in containers:
            resp = MeasurementLogisticsApi.get_measurements_in_container(self, cont)
            measurements.extend(resp)
        measurements = list(set(measurements))
        return measurements

    def biosamples_in_shipment(self, shipment: Shipment) -> List[Biosample]:
        """Returns a list of Biosamples in a Shipment."""
        measurements = self.measurements_in_shipment(shipment)
        biosample_ids = []
        for m in measurements:
            if m.biosample not in biosample_ids:
                biosample_ids.append(m.biosample)
        biosamples = [BiosampleApi.get_biosample(self, b) for b in biosample_ids]
        return biosamples

    def subjects_in_shipment(self, shipment: Shipment) -> List[Subject]:
        """Returns a list of Subjects in a Shipment."""
        biosamples = self.biosamples_in_shipment(shipment)
        subject_ids = []
        for b in biosamples:
            if b.subject not in subject_ids:
                subject_ids.append(b.subject)
        subjects = [SubjectApi.get_subject(self, s) for s in subject_ids]
        return subjects
