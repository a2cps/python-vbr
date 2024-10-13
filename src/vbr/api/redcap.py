from vbr.tableclasses import RcapTable, class_from_table

__all__ = ["RcapTableApi"]


class RcapTableApi(object):
    def get_redcap_tableclass(
        self, redcap_form_name: str, redcap_data: dict, **kwargs
    ) -> RcapTable:
        PARAMS = list(RcapTable.link_column_names())
        PARAMS.append("record_id")
        # Look up the table class
        tc = class_from_table("rcap_" + redcap_form_name)
        # Extend redcap_data dictionary with any provided kwargs on the allow list
        for p in PARAMS:
            if kwargs.get(p, None) is not None:
                redcap_data[p] = kwargs.get(p)
                # print('kwarg found: ', p, redcap_data[p])
        # Instantiate the VBR object
        instance = tc(**redcap_data)
        return instance

    def create_redcap_table_row(
        self, redcap_form_name: str, redcap_data: dict, **kwargs
    ) -> RcapTable:
        """Create a RcapTable-derived VBR record."""
        # TODO = fix this in RcapTable. I don't like this construction
        instance = self.get_redcap_tableclass(redcap_form_name, redcap_data, **kwargs)
        return self.vbr_client.create_row(instance)[0]

    def get_redcap_record_by_biosample_and_instance(
        self, redcap_form_name: str, biosample_id: str, subject_id: str, protocol_id: str, repeat_instance: str
        ) -> RcapTable:
        """Retrieve a Biosample by subject and protocol IDs."""
        redcap_form_name = 'rcap_'+redcap_form_name
        query = {
            "subject_id": {"operator": "=", "value": subject_id},
            "biosample_id": {"operator": "=", "value": biosample_id},
            "protocol_id": {"operator": "=", "value": protocol_id},
            "redcap_repeat_instance": {"operator": "=", "value": repeat_instance}
        }
        #patch for null values
        if repeat_instance == '' or repeat_instance is None:
            query["redcap_repeat_instance"] = {'operator': 'null', 'value': 'TRUE'}

        return self._get_row_from_table_with_query(redcap_form_name, query=query)

    def get_redcap_record_by_subject_and_protocol(
        self, redcap_form_name: str, subject_id: str, protocol_id: str
        ) -> RcapTable:
        """Retrieve a Biosample by subject and protocol IDs."""
        redcap_form_name = 'rcap_'+redcap_form_name
        query = {
            "subject_id": {"operator": "=", "value": subject_id},
            "protocol_id": {"operator": "=", "value": protocol_id}
            }
        return self._get_row_from_table_with_query(redcap_form_name, query=query)
    
    def update_redcap_record(
        self, redcap_form_name: str, redcap_record: RcapTable, rcap_row: RcapTable
        ) -> RcapTable:
        """Update RedCap row based on RedCap API response"""
        for k,v in redcap_record.dict().items():
            old_value = rcap_row.dict().get(k,None)
            if old_value is not None and old_value != v:
                setattr(rcap_row,k,v)
        rcap_row = self.vbr_client.update_row(rcap_row)
        return rcap_row