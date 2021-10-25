from vbr.tableclasses import class_from_table, RcapTable

__all__ = ['RcapTableApi']


class RcapTableApi(object):
    def create_redcap_table_row(self, redcap_form_name: str, redcap_data: dict,
                                **kwargs) -> RcapTable:
        """Create a RcapTable-derived VBR record."""
        # TODO = fix this in RcapTable. I don't like this construction
        PARAMS = list(RcapTable.link_column_names())
        PARAMS.append('record_id')
        # Look up the table class
        tc = class_from_table('rcap_' + redcap_form_name)
        # Extend redcap_data dictionary with any provided kwargs on the allow list
        for p in PARAMS:
            if kwargs.get(p, None) is not None:
                redcap_data[p] = kwargs.get(p)
                # print('kwarg found: ', p, redcap_data[p])
        # Instantiate the VBR object
        instance = tc(**redcap_data)
        return self.vbr_client.create_row(instance)[0]
